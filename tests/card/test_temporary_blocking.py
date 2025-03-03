import json
import time

import allure
import pytest
from pages.card.card_page import CardPage
from pages.card.change_blu_card_pages import ChangeBluCardPage
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


# Behaviors
# Behaviors
@allure.epic("Card Management")
@allure.feature("Card Freeze Functionality")
@allure.story("Temporarily block the card by toggling the freeze option")
# Suites
@allure.suite(f"version:{VERSION}")
@allure.sub_suite("Tests for Card Freeze Features")
# Severity Level
@allure.severity(allure.severity_level.CRITICAL)
# Links
@allure.link("https://jira.sdb247.com/secure/enav/#/5686?query=issue%3DQA-22654&offset=1&pageWidth=10&view=detail", name="Jira Task")
# Parameterization
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_temporary_blocking(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard

    # بارگذاری فایل JSON برای دریافت متون مرجع
    text_reference = load_text_reference()
    try:
        with allure.step("Click on 'card tab' button"):
            logger.info("کلیک روی دکمه 'تب کارت'...")
            dashboard_page = DashboardPage(driver)
            dashboard_page.card_tab_button()
            logger.info("دکمه 'تب کارت' کلیک شد.")

        with allure.step("Check and toggle the agreement switch"):
            # بررسی وضعیت اولیه تاگل
            card_page = CardPage(driver)

            initial_status = card_page.is_switch_on()
            logger.info(f"Initial switch status: {'ON' if initial_status else 'OFF'}")

            # اگر تاگل روشن است، آن را خاموش کنید
            if initial_status:
                logger.info("Switch is ON. Toggling to OFF...")
                card_page.freeze_toggle_switch()
                new_status = card_page.is_switch_on()
                assert not new_status, "Error: Switch did not toggle to OFF."
                logger.info("Switch successfully toggled to OFF.")
            else:
                logger.info("Switch is already OFF. No action needed.")


        with allure.step("Check and toggle the agreement switch"):
            initial_status = card_page.is_switch_on()
            logger.info(f"Initial switch status: {'ON' if initial_status else 'OFF'}")
            card_page.freeze_toggle_switch()
            with allure.step("Verify Freeze Card Toast Message"):
                logger.info("بررسی پیام تایید مسدود کردن کارت...")
                check_text_match(
                    card_page.toast_text(),
                    text_reference["card_page"]["freeze_toast"],
                    "پیام تایید مسدود کردن کارت"
                )
            new_status = card_page.is_switch_on()
            logger.info(f"Switch status after toggle: {'ON' if new_status else 'OFF'}")

        try:
            with allure.step("Check that 'Pin2' button is disabled"):
                logger.info("در حال بررسی وضعیت دکمه 'رمز دوم پویا'...")
                card_page.check_enable_pin2_button()
                logger.info("تست موفقیت‌آمیز بود. دکمه 'رمز دوم پویا' غیرفعال است.")
        except Exception as e:
            logger.error(f"خطایی رخ داد: {e}")
            screenshot_path = capture_screenshot(driver, "pin2_button_disabled_error")
            allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

        with allure.step("Verify 'Security Setting' Button is Disabled"):
            try:
                logger.info("در حال بررسی وضعیت دکمه 'تنظیمات امنیتی'...")
                card_page.check_enable_pin2_button()
                logger.info("دکمه 'تنظیمات امنیتی' غیرفعال است.")
            except Exception as e:
                logger.error(f"خطا در بررسی دکمه 'تنظیمات امنیتی': {e}")
                screenshot_path = capture_screenshot(driver, "security_setting_button_disabled_error")
                allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
                raise e

        with allure.step("Verify 'Blu Card Freeze' Button"):
            try:
                logger.info("در حال بررسی دکمه 'Blu Card Freeze'...")
                card_page.blu_card_freeze()
                logger.info("دکمه 'Blu Card Freeze' وجود دارد و نمایش داده شده است.")
            except Exception as e:
                logger.error(f"خطا در بررسی دکمه 'Blu Card Freeze': {e}")
                screenshot_path = capture_screenshot(driver, "blu_card_freeze_button_error")
                allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
                raise e

        with allure.step("Change Blu Card"):
            logger.info("کلیک روی 'تعویض بلوکارت'...")
            card_page.change_blu_card_button()
            logger.info("روی 'تعویض بلو کارت' کلیک شد.")

            try:
                logger.info("در حال بررسی وضعیت دکمه 'شماره کارت فعلی'...")
                change_blu_card = ChangeBluCardPage(driver)
                change_blu_card.same_pan_button()
                logger.info("دکمه 'شماره کارت فعلی' غیرفعال است.")
            except Exception as e:
                logger.error(f"خطا در بررسی دکمه 'شماره کارت فعلی': {e}")
                screenshot_path = capture_screenshot(driver, "same_pan_button_error")
                allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
                raise e

            logger.info("بازگشت به صفحه کارت...")
            change_blu_card.back_button()

        with allure.step("Unfreeze Card"):
            logger.info("در حال باز کردن مسدودی کارت...")
            card_page.freeze_toggle_switch()

            with allure.step("Verify Unfreeze Toast Message"):
                logger.info("بررسی پیام تایید رفع مسدودی کارت...")
                check_text_match(
                    card_page.toast_text(),
                    text_reference["card_page"]["unfreeze_toast"],
                    "پیام تایید رفع مسدودی کارت"
                )

            logger.info(f"وضعیت تاگل پس از رفع مسدودی: {'روشن' if card_page.is_switch_on() else 'خاموش'}")

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        screenshot_path = capture_screenshot(driver, "card_page_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e