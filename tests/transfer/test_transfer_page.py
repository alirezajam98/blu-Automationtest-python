import json
import allure
import pytest

from pages.dashboard.dashboard_page import DashboardPage
from pages.transfer.transfer_page import TransferPage
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


@allure.epic("Transfer")
@allure.feature("Transfer Page Verification")
@allure.story("Verify all text elements and functionality on Transfer page")
# Suites
@allure.suite(f"Version:{VERSION}")
@allure.sub_suite("Text and Functionality Verification for Transfer Page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["andauto1"], indirect=True)
def test_transfer_page(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard
    text_reference = load_text_reference()
    trx_texts = text_reference["transfer_page"]
    transfer_page = TransferPage(driver)
    try:
        with allure.step("Navigate to Transfer Tab"):
            logger.info("ورود به تب انتقال...")
            dashboard_page.transfer_tab_button()
            logger.info("وارد تب انتقال شد.")

        with allure.step("Close the onboarding page"):
            logger.info("بستن صفحه انبوردینگ...")
            transfer_page.close_onboarding()
            logger.info("صفحه انبوردینگ بسته شد.")

        with allure.step("Verify 'Transfer Title' Text"):
            logger.info("بررسی متن 'انتقال'...")
            check_text_match(
                transfer_page.get_transfer_page_title_text(),
                trx_texts["transfer_title"],
                "متن عنوان صفحه انتقال"
            )

        with allure.step("Verify 'Promo Title' Text"):
            logger.info("بررسی متن 'انتقال به مخاطبین'...")
            check_text_match(
                transfer_page.get_promo_title_text(),
                trx_texts["promo_title"],
                "متن عنوان تبلیغ"
            )

        with allure.step("Verify 'Promo Description' Text"):
            logger.info("بررسی متن توضیحات تبلیغ...")
            check_text_match(
                transfer_page.get_promo_description_text(),
                trx_texts["promo_description"],
                "متن توضیحات تبلیغ"
            )

        with allure.step("Verify 'Destinations Header' Text"):
            logger.info("بررسی متن 'مقصدها'...")
            check_text_match(
                transfer_page.get_destinations_header_text(),
                trx_texts["destinations_header"],
                "متن هدر مقصدها"
            )

        with allure.step("Verify 'Empty State Title' Text"):
            logger.info("بررسی متن 'مقصد انتقالی ندارید'...")
            check_text_match(
                transfer_page.get_empty_state_title_text(),
                trx_texts["empty_state_title"],
                "متن عنوان حالت خالی"
            )

        with allure.step("Verify 'Empty State Description' Text"):
            logger.info("بررسی متن 'اولین انتقال خود را انجام دهید'...")
            check_text_match(
                transfer_page.get_empty_state_description_text(),
                trx_texts["empty_state_description"],
                "متن توضیحات حالت خالی"
            )

        with allure.step("Click 'Cancel Button'"):
            logger.info("کلیک روی دکمه 'الان نه'...")
            transfer_page.click_cancel_button()
            logger.info("دکمه 'الان نه' کلیک شد.")
            logger.info("رفرش صفحه برای نمایش دوباره انتقال به مخاطبین...")
            transfer_page.scroll()
            logger.info("رفرش انجام شد.")
            logger.info("کلیک روی دکمه 'الان نه'...")
            transfer_page.click_cancel_button()
            logger.info("دکمه 'الان نه' کلیک شد.")

    except Exception as e:
        logger.error(f"خطا در بررسی صفحه انتقال: {e}")
        screenshot_path = capture_screenshot(driver, "transfer_page_error")
        allure.attach.file(screenshot_path, name="transfer Error", attachment_type=allure.attachment_type.PNG)
        raise e
