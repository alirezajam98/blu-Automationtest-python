import json
import allure
import pytest
from pages.card.card_page import CardPage
from pages.card.share_card_number_bottom_sheet import ShareCardNumberBottomSheet
from pages.dashboard.dashboard_page import DashboardPage
from utils.config import configure_logger, capture_screenshot
from utils.utils import normalize_card_number, check_text_match

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
@allure.feature("Copy & Share Functionalities")
@allure.story("Allow users to copy and share card number and sheba")
# Suites
@allure.suite(f"version:{VERSION}")
@allure.sub_suite("Tests for Copy & Share Features")
@allure.severity(allure.severity_level.CRITICAL)
# Links
@allure.link("https://jira.sdb247.com/secure/enav/#/5686?query=issue%3DQA-22654&offset=1&pageWidth=10&view=detail", name="Jira Task")
# Parameterization
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_share_card_number(login_and_dashboard):
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

        with allure.step("Verify Card Number from Blu Card"):
            logger.info("بررسی شماره کارت بلو کارت...")
            card_number_1 = card_page.card_number_text()
            normalized_card_1 = normalize_card_number(card_number_1)
            logger.info(f"شماره کارت بلو کارت: {normalized_card_1}")

        with allure.step("Verify Share Button Title"):
            logger.info("بررسی متن دکمه اشتراک‌گذاری شماره کارت و شبا...")
            check_text_match(
                card_page.share_card_number_button_title(),
                text_reference["card_page"]["shareButton"],
                "متن دکمه اشتراک‌گذاری شماره کارت و شبا"
            )

        with allure.step("Click Share Button"):
            logger.info("کلیک روی دکمه اشتراک‌گذاری شماره کارت و شبا...")
            card_page.share_card_number_button()
            logger.info("دکمه اشتراک‌گذاری شماره کارت و شبا کلیک شد.")

        with allure.step("Verify Card Number Title in Bottom Sheet"):
            logger.info("بررسی عنوان شماره کارت در باتم شیت...")
            share_bottom_sheet = ShareCardNumberBottomSheet(driver)
            check_text_match(
                share_bottom_sheet.card_number_title(),
                text_reference["card_page"]["card_number_title"],
                "عنوان شماره کارت در باتم شیت"
            )

        with allure.step("Verify Card Number in Bottom Sheet"):
            logger.info("بررسی شماره کارت در باتم شیت...")
            card_number_2 = share_bottom_sheet.card_number()
            normalized_card_2 = normalize_card_number(card_number_2)
            check_text_match(
                normalized_card_2,
                normalized_card_1,
                "شماره کارت در باتم شیت"
            )

        with allure.step("Verify Sheba Number Title in Bottom Sheet"):
            logger.info("بررسی عنوان شماره شبا در باتم شیت...")
            check_text_match(
                share_bottom_sheet.sheba_number_title(),
                text_reference["card_page"]["sheba_number_title"],
                "عنوان شماره شبا در باتم شیت"
            )

        with allure.step("Click Copy Card Number Button"):
            logger.info("کلیک روی دکمه کپی شماره کارت...")
            share_bottom_sheet.copy_card_number_button()
            logger.info("دکمه کپی شماره کارت کلیک شد.")

        with allure.step("Verify Toast for Copy Card Number"):
            logger.info("بررسی پیام تایید کپی شماره کارت...")
            check_text_match(
                share_bottom_sheet.toast_text(),
                text_reference["card_page"]["copy_card_number_toast_text"],
                "پیام تایید کپی شماره کارت"
            )

        with allure.step("Click Share Button"):
            logger.info("کلیک روی دکمه اشتراک‌گذاری شماره کارت و شبا...")
            card_page.share_card_number_button()
            logger.info("دکمه اشتراک‌گذاری شماره کارت و شبا کلیک شد.")

        with allure.step("Click Copy Sheba Number Button"):
            logger.info("کلیک روی دکمه کپی شماره شبا...")
            share_bottom_sheet.copy_sheba_number_button()
            logger.info("دکمه کپی شماره شبا کلیک شد.")

        with allure.step("Verify Toast for Copy Sheba Number"):
            logger.info("بررسی پیام تایید کپی شماره شبا...")
            check_text_match(
                share_bottom_sheet.toast_text(),
                text_reference["card_page"]["copy_sheba_number_toast_text"],
                "پیام تایید کپی شماره شبا"
            )

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        screenshot_path = capture_screenshot(driver, "share_card_number_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
