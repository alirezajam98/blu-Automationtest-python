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
@allure.story("Transfer to Contact")
@allure.suite(f"Version: {VERSION}")
@allure.sub_suite("Transfer to contact")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_transfer_to_contacts_flow(login_and_dashboard):
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
        transfer_to_contact = TransferToContactPage(driver)
        with allure.step("Enable Transfer to Contacts"):
            logger.info("فعال‌سازی انتقال وجه به مخاطبین...")
            security_page.click_transfer_to_contacts()
            transfer_to_contact.enable_transfer_to_contacts()
            # پذیرش شرایط و قوانین
            logger.info("فعال‌سازی موافقت با قوانین...")
            transfer_to_contact.accept_terms_and_conditions()

            # کلیک روی دکمه تأیید
            transfer_to_contact.click_confirm_button()
            transfer_to_contact.click_confirm_button()
            transfer_to_contact.click_confirm_button_sysytem_allow_permission()
            logger.info("فعال‌سازی ")

        with allure.step("Disable Transfer to Contacts"):
            logger.info("غیر فعال‌سازی ")
            security_page.click_transfer_to_contacts()
            transfer_to_contact.enable_transfer_to_contacts()
            transfer_to_contact.confirm_disable()
    except Exception as e:
        capture_screenshot(driver, "transfer_to_contacts_flow")
        logger.error(f"خطا در بررسی جریان انتقال وجه به مخاطبین: {str(e)}")
        raise
