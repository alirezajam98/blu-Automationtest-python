import json
import allure
import pytest

from pages.kyc.kyc_pages import SelectJobPage
from pages.setting.account.account_page import AccountPage
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
@allure.feature("Account Page")
@allure.story("Change Job")
@allure.suite(f"Version: {VERSION}")
@allure.sub_suite("Job Title Modification Test")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_change_job(login_and_dashboard):
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

        # کلیک روی گزینه تغییر شغل
        with allure.step("Navigate to Change Job Page"):
            logger.info("کلیک روی گزینه تغییر شغل...")
            account_page.click_change_job_option()

        with allure.step("Select job for user"):
            logger.info("کلیک بر روی اولین شغل")
            select_job_page = SelectJobPage(driver)
            select_job_page.select_job()
            logger.info("اولین شغل از لیست انتخاب شد.")
            logger.info("کلیک روی دکمه تایید تغییر شغل...")
            select_job_page.click_confirm_job()
            logger.info("دکمه 'تایید شغل' کلیک شد.")

        with allure.step("Verify Confirmation Toast Message for Job Change"):
            logger.info("بررسی پیام تایید تغییر شغل...")
            check_text_match(
                account_page.toast_text(),
                text_reference["account_page"]["job_toast"],
                "پیام تایید تغییر شغل:"
            )

    except Exception as e:
        capture_screenshot(driver, "job_change_verification")
        logger.error(f"خطا هنگام بررسی تغییر شغل: {str(e)}")
        raise
