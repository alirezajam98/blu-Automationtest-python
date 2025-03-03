import json
import allure
import pytest

from pages.setting.account.account_page import AccountPage, BankAccountBottomSheet, CloseAccountConfirmationDialog
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
@allure.story("Verify all displayed texts on Account Page")
@allure.suite(f"Version: {VERSION}")
@allure.sub_suite("Job Title Modification Test")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
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

        # کلیک روی گزینه حساب بانکی
        account_page.click_bank_account_option()
        bottom_sheet = BankAccountBottomSheet(driver)

        # بررسی اطلاعات باتم‌شیت
        with allure.step("Verify Bank Account Bottom Sheet"):
            logger.info("بررسی اطلاعات باتم‌شیت حساب بانکی...")
            check_text_match(
                bottom_sheet.title(),
                text_reference["bank_account_bottom_sheet"]["title"],
                "عنوان باتم‌شیت"
            )
            check_text_match(
                bottom_sheet.description(),
                text_reference["bank_account_bottom_sheet"]["description"],
                "توضیحات باتم‌شیت"
            )
            check_text_match(
                bottom_sheet.join_date(),
                text_reference["bank_account_bottom_sheet"]["join_date_label"],
                "تاریخ پیوستن به بلو"
            )
            check_text_match(
                bottom_sheet.account_type(),
                text_reference["bank_account_bottom_sheet"]["account_type_label"],
                "نوع حساب"
            )

            check_text_match(
                bottom_sheet.close_account_button(),
                text_reference["bank_account_bottom_sheet"]["close_account_button"],
                "دکمه بستن حساب"
            )
            logger.info("تمامی اطلاعات باتم‌شیت حساب بانکی بررسی شد.")

        # بررسی مقادیر واقعی اطلاعات حساب
        with allure.step("Verify Account Details"):
            logger.info("بررسی مقادیر واقعی اطلاعات حساب...")
            check_text_match(
                bottom_sheet.get_account_holder_name(),
                text_reference["bank_account_bottom_sheet"]["account_holder_value"],
                "نام دارنده حساب"
            )
            check_text_match(
                bottom_sheet.get_join_date_value(),
                text_reference["bank_account_bottom_sheet"]["join_date_value"],
                "تاریخ پیوستن به بلو"
            )
            check_text_match(
                bottom_sheet.get_account_type_value(),
                text_reference["bank_account_bottom_sheet"]["account_type_value"],
                "نوع حساب"
            )
            check_text_match(
                bottom_sheet.get_account_number_value(),
                text_reference["bank_account_bottom_sheet"]["account_number_value"],
                "شماره حساب"
            )
            check_text_match(
                bottom_sheet.get_iban_number_value(),
                text_reference["bank_account_bottom_sheet"]["iban_number_value"],
                "شماره شبا"
            )

            logger.info("تمامی مقادیر واقعی اطلاعات حساب بررسی شد.")

        # تعامل با دکمه‌های باتم‌شیت
        with allure.step("Interact with Bottom Sheet Buttons"):
            logger.info("تعامل با دکمه‌های باتم‌شیت...")

            # کلیک روی دکمه "سایر حساب‌های بانک سامان"
            bottom_sheet.click_other_saman_accounts()
            logger.info("کلیک روی دکمه سایر حساب‌های بانک سامان انجام شد.")

            # بازگشت به صفحه قبلی (باتم‌شیت حساب بانکی)
            driver.back()
            account_page.click_bank_account_option()
            logger.info("بازگشت به صفحه باتم‌شیت حساب بانکی.")

            # کلیک روی دکمه "بستن حساب"
            bottom_sheet.click_close_account()
            logger.info("کلیک روی دکمه بستن حساب انجام شد.")
            # مدیریت دیالوگ تأیید
            confirmation_dialog = CloseAccountConfirmationDialog(driver)

            # بررسی عناصر دیالوگ
            check_text_match(
                confirmation_dialog.get_dialog_title(),
                text_reference["close_account_dialog"]["title"],
                "عنوان دیالوگ تأیید"
            )

            check_text_match(
                confirmation_dialog.get_dialog_description(),
                text_reference["close_account_dialog"]["description"],
                "توضیحات دیالوگ تأیید"
            )

            # کلیک روی دکمه انصراف
            confirmation_dialog.click_cancel_button()
            logger.info("کلیک روی دکمه انصراف انجام شد.")


    except Exception as e:
        capture_screenshot(driver, "account_page_verification")
        logger.error(f"خطا هنگام بررسی متن‌های صفحه حساب کاربری: {str(e)}")
        raise
