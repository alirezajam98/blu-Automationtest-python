import json
import time

import allure
import pytest
from pages.card.card_page import CardPage
from pages.card.dynamic_pin_bottom_sheet import DynamicPinBottomSheet
from pages.dashboard.dashboard_page import DashboardPage
from utils.config import configure_logger, capture_screenshot
from utils.utils import check_text_match, normalize_card_number, is_six_digit_persian_number

# تنظیمات لاگ
logger = configure_logger()


# تابعی برای بارگذاری فایل JSON
def load_text_reference():
    with open('utils/text_reference.json', 'r', encoding='utf-8') as f:
        return json.load(f)


# بارگذاری نسخه از فایل
with open('utils/version.json') as f:
    config = json.load(f)
    VERSION = config.get("version", "unknown_version")  # مقدار پیش‌فرض در صورت نبود نسخه


@allure.epic("Card Management")
@allure.feature("Dynamic Second Password")
@allure.story("Generate Dynamic Second Password for user")
# Suites
@allure.suite(f"version:{VERSION}")
@allure.sub_suite("Tests for Dynamic Second Password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://jira.sdb247.com/secure/enav/#/5686?query=issue%3DQA-22654&offset=1&pageWidth=10&view=detail",
             name="Jira Task")
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_dynamic_pin(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard

    # بارگذاری فایل JSON برای دریافت متون مرجع
    text_reference = load_text_reference()

    try:
        with allure.step("Navigate to Card Tab"):
            logger.info("ورود به تب کارت...")
            dashboard_page.card_tab_button()
            logger.info("وارد تب کارت شد.")

        with allure.step("Open Blu Card"):
            logger.info("کلیک روی کارت بلو...")
            card_page = CardPage(driver)
            card_page.scroll_menu()
            card_page.blu_card()
            logger.info("روی کارت بلو کلیک شد.")

        with allure.step("Verify Card Number from Blu Card Icon"):
            logger.info("بررسی شماره کارت بلو کارت...")
            card_number_1 = card_page.card_number_text()
            normalized_card_1 = normalize_card_number(card_number_1)
            logger.info(f"شماره کارت بلو کارت: {normalized_card_1}")

        with allure.step("Verify Dynamic PIN Button Title"):
            logger.info("بررسی متن دکمه رمز دوم پویا...")
            check_text_match(
                card_page.pin2_button_title(),
                text_reference["card_page"]["pin2_bottom_sheet_title"],
                "متن دکمه رمز دوم پویا"
            )

        with allure.step("Open Dynamic PIN Bottom Sheet"):
            logger.info("کلیک روی دکمه رمز دوم پویا...")
            dynamic_pin_bottom_sheet = DynamicPinBottomSheet(driver)
            card_page.pin2_button()
            logger.info("باتم شیت رمز دوم پویا باز شد.")

        with allure.step("Verify Dynamic PIN Bottom Sheet Title"):
            logger.info("بررسی عنوان باتم شیت رمز دوم پویا...")
            check_text_match(
                dynamic_pin_bottom_sheet.pin2_bottom_sheet_title(),
                text_reference["card_page"]["pin2_bottom_sheet_title"],
                "عنوان باتم شیت رمز دوم پویا"
            )

        with allure.step("Verify Card Number in Dynamic PIN Bottom Sheet"):
            logger.info("بررسی شماره کارت در باتم شیت...")
            card_number_2 = dynamic_pin_bottom_sheet.card_number()
            normalized_card_2 = normalize_card_number(card_number_2)
            check_text_match(
                normalized_card_2,
                normalized_card_1,
                "شماره کارت در باتم شیت"
            )

        with allure.step("Validate Dynamic PIN Format"):
            logger.info("بررسی فرمت رمز دوم پویا...")
            time.sleep(10)
            dynamic_code = dynamic_pin_bottom_sheet.dynamic_pin()
            assert is_six_digit_persian_number(dynamic_code), f"رمز دوم پویا معتبر نیست: {dynamic_code}"
            logger.info(f"رمز دوم پویا صحیح است: {dynamic_code}")

        with allure.step("Verify Copy Dynamic PIN Button Title"):
            logger.info("بررسی متن دکمه کپی کردن رمز دوم پویا...")
            check_text_match(
                dynamic_pin_bottom_sheet.copy_dynamic_button_pin_title(),
                text_reference["card_page"]["copy_dynamic_button_pin_title"],
                "متن دکمه کپی کردن رمز دوم پویا"
            )

        with allure.step("Click Copy Dynamic PIN Button"):
            logger.info("کلیک روی دکمه کپی رمز دوم پویا...")
            dynamic_pin_bottom_sheet.copy_dynamic_button_pin()
            logger.info("رمز دوم پویا کپی شد.")

        with allure.step("Verify Copy Dynamic PIN Toast Message"):
            logger.info("بررسی پیام تایید کپی رمز دوم پویا...")
            check_text_match(
                dynamic_pin_bottom_sheet.toast_text(),
                text_reference["card_page"]["pin2_toast_text"],
                "پیام تایید کپی رمز دوم پویا"
            )

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        screenshot_path = capture_screenshot(driver, "dynamic_pin_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
