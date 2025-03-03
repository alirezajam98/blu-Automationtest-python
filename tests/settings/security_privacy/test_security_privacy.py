import json
import allure
import pytest
from pages.setting.security_privacy.security_privacy_page import SecurityPrivacyPage
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
@allure.story("Verify Security & Privacy Page Features")
@allure.suite(f"Version: {VERSION}")
@allure.sub_suite("Security Settings")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_security_privacy_page(login_and_dashboard):
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

        with allure.step("Verify Page Title"):
            logger.info("بررسی عنوان صفحه...")
            check_text_match(
                security_page.get_page_title(),
                text_reference["security_privacy_page"]["title"],
                "عنوان صفحه امنیت و حریم خصوصی"
            )

        with allure.step("Verify Menu Items Text"):
            logger.info("بررسی متن آیتم‌های منو...")
            check_text_match(
                security_page.get_change_password_text(),
                text_reference["security_privacy_page"]["change_password"],
                "متن گزینه تغییر رمز عبور"
            )
            check_text_match(
                security_page.get_transaction_password_text(),
                text_reference["security_privacy_page"]["transaction_password"],
                "متن گزینه رمز تراکنش"
            )
            check_text_match(
                security_page.get_my_devices_text(),
                text_reference["security_privacy_page"]["my_devices"],
                "متن گزینه دستگاه‌های من"
            )
            check_text_match(
                security_page.get_transfer_to_contacts_text(),
                text_reference["security_privacy_page"]["transfer_to_contacts"],
                "متن گزینه انتقال وجه به مخاطبین"
            )
            check_text_match(
                security_page.get_logout_text(),
                text_reference["security_privacy_page"]["logout"],
                "متن گزینه خروج از حساب کاربری"
            )

        with allure.step("Test Change Password Flow"):
            logger.info("شروع تست جریان تغییر رمز عبور...")
            security_page.click_change_password()
            # اضافه کردن تست‌های مربوط به صفحه تغییر رمز عبور
            driver.back()

        with allure.step("Test Transaction Password Flow"):
            logger.info("شروع تست جریان رمز تراکنش...")
            security_page.click_transaction_password()
            # اضافه کردن تست‌های مربوط به صفحه رمز تراکنش
            driver.back()

    except Exception as e:
        capture_screenshot(driver, "security_privacy_verification")
        logger.error(f"خطا در بررسی صفحه امنیت و حریم خصوصی: {str(e)}")
        raise
