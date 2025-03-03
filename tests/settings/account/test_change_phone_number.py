import json
import allure
import pytest

from pages.setting.account.account_page import AccountPage
from pages.setting.account.change_phone_page import ChangePhonePage
from pages.setting.settings_page import SettingPage
from utils.config import configure_logger, capture_screenshot
from utils.utils import check_text_match, mobile_number_generator

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
@allure.feature("Account Page")
@allure.story("Change Phone Number")
@allure.suite(f"Version: {VERSION}")
@allure.sub_suite("Phone Number Title Modification Test")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend109"], indirect=True)
def test_verify_account_page(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard

    # بارگذاری فایل JSON
    text_reference = load_text_reference()

    try:
        with allure.step("Navigate to Settings and Account Page"):
            logger.info("ورود به تب تنظیمات و صفحه حساب کاربری...")
            dashboard_page.click_settings_button()
            settings_page = SettingPage(driver)
            settings_page.click_account()
            logger.info("وارد صفحه حساب کاربری شد.")

        account_page = AccountPage(driver)

        # بررسی عنوان صفحه حساب کاربری
        with allure.step("Verify Account Page Title"):
            logger.info("بررسی عنوان صفحه حساب کاربری...")
            check_text_match(
                account_page.get_account_page_title(),
                text_reference["account_page"]["title"],
                "عنوان صفحه حساب کاربری"
            )

        # کلیک روی گزینه تغییر شماره تلفن همراه
        with allure.step("Navigate to Change Phone Page"):
            logger.info("کلیک روی گزینه تغییر شماره تلفن همراه...")
            account_page.click_change_phone_option()

        # ایجاد شیء صفحه تغییر شماره تلفن
        change_phone_page = ChangePhonePage(driver)

        # بررسی عنوان صفحه تغییر شماره تلفن
        with allure.step("Verify Change Phone Page Title"):
            logger.info("بررسی عنوان صفحه تغییر شماره تلفن...")
            check_text_match(
                change_phone_page.get_page_title(),
                text_reference["change_phone_page"]["title"],
                "عنوان صفحه تغییر شماره تلفن"
            )

        # بررسی متن راهنمای فیلد ورودی
        with allure.step("Verify Phone Input Hint"):
            logger.info("بررسی متن راهنمای فیلد ورودی شماره تلفن...")
            check_text_match(
                change_phone_page.get_input_hint(),
                text_reference["change_phone_page"]["input_hint"],
                "متن راهنمای فیلد ورودی شماره تلفن"
            )

        # بررسی متن راهنمای صفحه
        with allure.step("Verify Guide Text"):
            logger.info("بررسی متن راهنمای صفحه...")
            check_text_match(
                change_phone_page.get_guide_text(),
                text_reference["change_phone_page"]["guide_text"],
                "متن راهنمای صفحه"
            )

        # وارد کردن شماره تلفن جدید
        with allure.step("Enter New Phone Number"):
            logger.info("وارد کردن شماره تلفن جدید...")
            phone_number = mobile_number_generator()
            change_phone_page.enter_phone_number(phone_number)

        # بررسی فعال بودن دکمه ادامه
        with allure.step("Verify Next Button State"):
            logger.info("بررسی فعال بودن دکمه ادامه...")
            assert change_phone_page.is_next_button_enabled(), "دکمه ادامه غیرفعال است."

        # کلیک روی دکمه ادامه
        with allure.step("Click Next Button"):
            logger.info("کلیک روی دکمه ادامه...")
            change_phone_page.click_next_button()

        with allure.step("Verify Confirmation Toast Message"):
            logger.info("بررسی پیام تایید تغییر شماره تلفن...")
            check_text_match(
                account_page.toast_text(),
                text_reference["account_page"]["change_number_toast"],
                "پیام تایید شماره تلفن"
            )

    except Exception as e:
        capture_screenshot(driver, "change_phone_page_verification")
        logger.error(f"خطا هنگام بررسی صفحه تغییر شماره تلفن: {str(e)}")
        raise