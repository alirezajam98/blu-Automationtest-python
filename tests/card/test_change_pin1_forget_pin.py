import json
import allure
import pytest
from pages.card.card_page import CardPage
from pages.card.card_security_setting_page import CardSecuritySettingsPages
from utils.config import configure_logger, capture_screenshot
from utils.utils import check_text_match

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
@allure.feature("Forgot First Password (PIN1)")
@allure.story("Allow users to reset their first password (PIN1)")
# Suites
@allure.suite(f"Version:{VERSION}")
@allure.sub_suite("Tests for Resetting First Password (PIN1)")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://jira.sdb247.com/secure/enav/#/5686?query=issue%3DQA-22654&offset=1&pageWidth=10&view=detail",
             name="Jira Task")
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_change_pin1_forget_pin(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard

    # بارگذاری فایل JSON برای دریافت متون مرجع
    text_reference = load_text_reference()

    try:
        with allure.step("Navigate to Card Tab"):
            logger.info("ورود به تب کارت...")
            dashboard_page.card_tab_button()
            logger.info("وارد تب کارت شد.")

        with allure.step("Verify 'Security Settings' Button Text"):
            logger.info("بررسی متن دکمه تنظیمات امنیتی...")
            card_page = CardPage(driver)
            check_text_match(
                card_page.card_security_setting_button_title(),
                text_reference["card_page"]["card_security_setting_button_title"],
                "متن دکمه تنظیمات امنیتی"
            )

        with allure.step("Click on 'Security Settings' Button"):
            logger.info("کلیک روی دکمه تنظیمات امنیتی...")
            card_page.card_security_setting_button()
            logger.info("روی دکمه تنظیمات امنیتی کلیک شد.")

        with allure.step("Verify 'Forgot First Password' Button Text"):
            logger.info("بررسی متن دکمه فراموشی رمز اول...")
            card_security_setting_pages = CardSecuritySettingsPages(driver)
            check_text_match(
                card_security_setting_pages.change_first_password_button_title(),
                text_reference["card_page"]["change_first_password_button"],
                "متن دکمه فراموشی رمز اول"
            )

        with allure.step("Click on 'Forgot First Password' Button"):
            logger.info("کلیک روی دکمه فراموشی رمز اول...")
            card_security_setting_pages.forgot_first_password_button()
            logger.info("روی دکمه فراموشی رمز اول کلیک شد.")

        with allure.step("Validate 'Forgot First Password' Page Titles"):
            logger.info("بررسی عنوان صفحه فراموشی رمز اول...")
            check_text_match(
                card_security_setting_pages.forgot_first_password_page_title(),
                text_reference["card_page"]["forgot_first_password"],
                "عنوان صفحه فراموشی رمز اول"
            )
            check_text_match(
                card_security_setting_pages.set_password_page_subtitle(),
                text_reference["card_page"]["set_password_page_subtitle"],
                "زیرعنوان صفحه فراموشی رمز اول"
            )

        with allure.step("Validate Password Fields"):
            logger.info("بررسی فیلدهای رمز جدید و تکرار رمز...")
            check_text_match(
                card_security_setting_pages.set_password_field_text(),
                text_reference["card_page"]["password_field"],
                "متن فیلد رمز جدید"
            )
            check_text_match(
                card_security_setting_pages.set_password_confirm_field_text(),
                text_reference["card_page"]["confirm_password_field"],
                "متن فیلد تکرار رمز جدید"
            )

        with allure.step("Test Various Error Scenarios"):
            logger.info("بررسی سناریوهای مختلف خطا...")

            # بررسی خطای خالی بودن فیلدها
            logger.info("بررسی خطای خالی بودن فیلدها...")
            driver.hide_keyboard()

            card_security_setting_pages.confirm_button()
            check_text_match(
                card_security_setting_pages.password_len_error(),
                text_reference["card_page"]["password_error"],
                "خطای خالی بودن فیلد رمز"
            )
            check_text_match(
                card_security_setting_pages.password_confirm_len_error(),
                text_reference["card_page"]["password_confirm_error"],
                "خطای خالی بودن فیلد تکرار رمز"
            )

            # بررسی خطای کوتاه بودن رمز
            logger.info("بررسی خطای کوتاه بودن رمز...")
            card_security_setting_pages.input_password("123")
            card_security_setting_pages.confirm_button()
            check_text_match(
                card_security_setting_pages.password_len_error(),
                text_reference["card_page"]["password_error"],
                "خطای کوتاه بودن رمز"
            )
            card_security_setting_pages.clear_input_password()

            # بررسی خطای عدم تطابق رمز و تکرار رمز
            logger.info("بررسی خطای عدم تطابق رمز و تکرار رمز...")
            card_security_setting_pages.input_password("1234")
            card_security_setting_pages.input_confirm_password("4321")
            card_security_setting_pages.confirm_button()
            check_text_match(
                card_security_setting_pages.password_not_match_error(),
                text_reference["card_page"]["password_confirm_not_match"],
                "خطای عدم تطابق رمز"
            )
            card_security_setting_pages.clear_input_password()
            card_security_setting_pages.clear_input_confirm_password()

        with allure.step("Set and Confirm New Password"):
            logger.info("تنظیم و تایید رمز جدید...")
            card_security_setting_pages.input_password("1234")
            card_security_setting_pages.input_confirm_password("1234")
            card_security_setting_pages.confirm_button()
            logger.info("رمز جدید با موفقیت تنظیم شد.")

        with allure.step("Verify Confirmation Toast Message"):
            logger.info("بررسی پیام تایید تغییر رمز...")
            check_text_match(
                card_page.toast_text(),
                text_reference["card_page"]["toast_confirmed_password"],
                "پیام تایید تغییر رمز"
            )

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        screenshot_path = capture_screenshot(driver, "forgot_pin1_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
