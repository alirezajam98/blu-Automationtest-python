import json
import allure
import pytest

from pages.setting.security_privacy.change_password_page import ChangePasswordPage
from pages.setting.security_privacy.security_privacy_page import SecurityPrivacyPage
from pages.setting.settings_page import SettingPage
from utils.config import configure_logger, capture_screenshot
from utils.utils import check_text_match, update_accounts, load_accounts

# تنظیمات لاگ
logger = configure_logger()


def load_text_reference():
    with open('utils/text_reference.json', 'r', encoding='utf-8') as f:
        return json.load(f)


with open('utils/version.json') as f:
    config = json.load(f)
    VERSION = config.get("version", "unknown_version")


@allure.epic("Profile")
@allure.feature("Security & Privacy Page")
@allure.story("Change Password Functionality")
@allure.suite(f"Version: {VERSION}")
@allure.sub_suite("Password Management")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_change_password(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard
    text_reference = load_text_reference()
    accounts = load_accounts()
    username = "suspeeeend106"  # یا دریافت از پارامتر تست

    # دریافت پسوردهای قدیم و جدید
    old_password = accounts[username]["pass1"]
    new_password = accounts[username]["pass2"]
    try:
        with allure.step("Navigate to Change Password Page"):
            logger.info("ورود به صفحه تغییر رمز عبور...")
            dashboard_page.click_settings_button()
            settings_page = SettingPage(driver)
            settings_page.click_security_privacy()
            security_page = SecurityPrivacyPage(driver)
            security_page.click_change_password()
            logger.info("وارد صفحه تغییر رمز عبور شد.")

        change_password_page = ChangePasswordPage(driver)

        with allure.step("Verify Page Title"):
            logger.info("بررسی عنوان صفحه...")
            check_text_match(
                change_password_page.get_page_title(),
                text_reference["change_password_page"]["title"],
                "عنوان صفحه تغییر رمز عبور"
            )

        # تست ۲: رمز عبور فعلی اشتباه
        with allure.step("Incorrect Old Password"):
            logger.info("رمز عبور فعلی اشتباه...")
            change_password_page.enter_old_password("WrongPass")
            change_password_page.enter_new_password("NewPass123")
            change_password_page.click_confirm_button()
            error_message = change_password_page.get_error_message()
            check_text_match(
                error_message,
                text_reference["change_password_page"]["incorrect_old_password_error"],
                "پیام خطای رمز عبور فعلی اشتباه"
            )

        # تست ۳: رمز عبور جدید نامعتبر
        with allure.step("Invalid New Password"):
            logger.info("رمز عبور جدید نامعتبر...")
            change_password_page.enter_old_password(old_password)
            change_password_page.enter_new_password("short")

        # تست ۴: رمز عبور جدید و قدیم یکسان
        with allure.step("New Password Same as Old Password"):
            logger.info("رمز عبور جدید و قدیم یکسان...")
            change_password_page.enter_old_password(old_password)
            change_password_page.enter_new_password(old_password)
            change_password_page.click_confirm_button()
            error_message = change_password_page.get_error_message()
            check_text_match(
                error_message,
                text_reference["change_password_page"]["same_password_error"],
                "پیام خطای یکسان بودن رمز عبور جدید و قدیم"
            )

            #  رمز عبور فعلی صحیح و رمز عبور جدید معتبر
            with allure.step("Correct Old Password and Valid New Password"):
                logger.info("رمز عبور فعلی صحیح و رمز عبور جدید معتبر...")
                change_password_page.enter_old_password(old_password)
                change_password_page.enter_new_password(new_password)
                assert change_password_page.is_confirm_button_enabled(), "دکمه تأیید غیرفعال است"
                change_password_page.click_confirm_button()
                # انتظار برای موفقیت‌آمیز بودن تغییر رمز عبور
                logger.info("رمز عبور با موفقیت تغییر کرد.")

            update_accounts("suspeeeend106", new_password, old_password)

            # with allure.step("Reset password to default Aa123456"):
            #     logger.info("رمز عبور فعلی صحیح و رمز عبور جدید معتبر...")
            #     dashboard_page.click_settings_button()
            #     settings_page.click_security_privacy()
            #     security_page.click_change_password()
            #     change_password_page.enter_old_password("Bb123456")
            #     change_password_page.enter_new_password("Aa123456")
            #     assert change_password_page.is_confirm_button_enabled(), "دکمه تأیید غیرفعال است"
            #     change_password_page.click_confirm_button()
            #     # انتظار برای موفقیت‌آمیز بودن تغییر رمز عبور
            #     logger.info("رمز عبور با موفقیت ریست شد.")

    except Exception as e:
        capture_screenshot(driver, "change_password_verification")
        logger.error(f"خطا در بررسی صفحه تغییر رمز عبور: {str(e)}")
        raise
