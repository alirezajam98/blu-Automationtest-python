import json
import allure
import pytest
from pages.setting.security_privacy.security_privacy_page import SecurityPrivacyPage
from pages.setting.security_privacy.transfer_to_contact_page import TransferToContactPage
from pages.setting.settings_page import SettingPage
from utils.config import configure_logger, capture_screenshot

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
@allure.story("LogOut from account")
@allure.suite(f"Version: {VERSION}")
@allure.sub_suite("LogOut")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_logout(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard
    text_reference = load_text_reference()
    dashboard_page.click_settings_button()

    try:
        with allure.step("Navigate to Security & Privacy Page"):
            logger.info("ورود به صفحه امنیت و حریم خصوصی...")
            settings_page = SettingPage(driver)
            settings_page.click_security_privacy()
            logger.info("وارد صفحه امنیت و حریم خصوصی شد.")

        security_page = SecurityPrivacyPage(driver)

        with allure.step("Click on LogOut and reject"):
            logger.info("کلیک روی دکمه خروج از حساب کاربری...")
            security_page.click_logout()
            logger.info("روی دکمه خروح از حساب کلیک شد.")
            logger.info("کلیک روی دکمه انصراف در مودال خروج از حساب کاربری...")
            security_page.cancel_logout()
            logger.info("روی انصراف در مودال خروج از حساب کاربری کلیک شد.")

        with allure.step("Click on LogOut and Confirm"):
            logger.info("کلیک روی دکمه خروج از حساب کاربری...")
            security_page.click_logout()
            logger.info("روی دکمه خروح از حساب کلیک شد.")
            logger.info("کلیک روی دکمه خروج در مودال خروج از حساب کاربری...")
            security_page.confirm_logout()
            logger.info("روی خروج در مودال خروج از حساب کاربری کلیک شد.")

    except Exception as e:
        capture_screenshot(driver, "transfer_to_contacts_flow")
        logger.error(f"خطا در بررسی جریان انتقال وجه به مخاطبین: {str(e)}")
        raise
