import json
import allure
import pytest
from pages.setting.security_privacy.security_privacy_page import SecurityPrivacyPage
from pages.setting.security_privacy.transaction_pin_page import TransactionPinPage
from pages.setting.settings_page import SettingPage
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


@allure.epic("Profile")
@allure.feature("Security & Privacy Page")
@allure.story("Transaction pin")
@allure.suite(f"Version: {VERSION}")
@allure.sub_suite("Transaction pin")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_transaction_password_flow(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard
    text_reference = load_text_reference()

    try:
        with allure.step("Navigate to Security & Privacy Page"):
            logger.info("ورود به صفحه امنیت و حریم خصوصی...")
            dashboard_page.click_settings_button()
            settings_page = SettingPage(driver)
            settings_page.click_security_privacy()
            logger.info("وارد صفحه امنیت و حریم خصوصی شد.")

        security_page = SecurityPrivacyPage(driver)
        transaction_pin_page = TransactionPinPage(driver)
        with allure.step("Enable Transaction Password"):
            logger.info("فعال‌سازی رمز تراکنش...")
            security_page.click_transaction_password()
            transaction_pin_page.enable_transaction_password()
            logger.info("وارد کردن رمز 1111")

            # وارد کردن رمز تراکنش
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            logger.info("وارد کردن مجدد رمز 1111")
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()

            # بررسی فعال بودن رمز تراکنش
            # assert transaction_pin_page.is_transaction_password_enabled(), "رمز تراکنش فعال نشده است."

        with allure.step("Change Transaction Password"):
            logger.info("تغییر رمز تراکنش...")
            transaction_pin_page.click_change_transaction_password()
            logger.info("رمز عبور فعلی..")
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            logger.info("رمز عبور جدید..")
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            logger.info("تکرار رمز عبور جدید..")
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            # بررسی فعال بودن رمز تراکنش پس از تغییر
            # assert transaction_pin_page.is_transaction_password_enabled(), "رمز تراکنش پس از تغییر فعال نیست."
        with allure.step("Disable Transaction Password"):
            transaction_pin_page.enable_transaction_password()
            logger.info("تکرار رمز عبور جدید..")
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
            transaction_pin_page.enter_transaction_password()
    except Exception as e:
        capture_screenshot(driver, "transaction_password_flow")
        logger.error(f"خطا در بررسی جریان رمز تراکنش: {str(e)}")
        raise
