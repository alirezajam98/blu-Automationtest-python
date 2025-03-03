import json
import allure
import pytest

from pages.dashboard.box.box_page import BoxPage
from pages.dashboard.dashboard_page import DashboardPage
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


@allure.epic("Box")
@allure.feature("Box Page Verification")
@allure.story("Verify all text elements on Box page after closing onboarding")
# Suites
@allure.suite(f"Version:{VERSION}")
@allure.sub_suite("Text Verification for Box Page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_box_page(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard
    text_reference = load_text_reference()
    box_texts = text_reference["box_page"]
    box_page = BoxPage(driver)
    try:
        with allure.step("Navigate to Box Tab"):
            logger.info("ورود به تب باکس...")
            dashboard_page.click_box_button()
            logger.info("وارد تب باکس شد.")

        with allure.step("Close the onboarding page"):
            logger.info("بستن صفحه انبوردینگ...")
            box_page.close_onboarding()
            logger.info("صفحه انبوردینگ بسته شد.")

        with allure.step("Verify Box Page is Displayed"):
            logger.info("بررسی نمایش صفحه باکس...")
            assert box_page.is_box_page_displayed(), "صفحه باکس بعد از بستن انبوردینگ نمایش داده نشده است."
            logger.info("صفحه باکس نمایش داده شد.")

        with allure.step("Verify '۰ ریال' Text"):
            logger.info("بررسی متن '۰ ریال'...")
            check_text_match(
                box_page.get_box_deposit_text(),
                box_texts["box_deposit_text"],
                "متن '۰ ریال'"
            )

        with allure.step("Verify 'موجودی باکس‌ها' Text"):
            logger.info("بررسی متن 'موجودی باکس‌ها'...")
            check_text_match(
                box_page.get_box_deposit_description(),
                box_texts["box_deposit_description"],
                "متن 'موجودی باکس‌ها'"
            )

        with allure.step("Verify 'باکس فعالی ندارید' Text"):
            logger.info("بررسی متن 'باکس فعالی ندارید'...")
            check_text_match(
                box_page.get_no_active_box_title(),
                box_texts["no_active_box_title"],
                "متن 'باکس فعالی ندارید'"
            )

    except Exception as e:
        logger.error(f"خطا در بررسی صفحه باکس: {e}")
        screenshot_path = capture_screenshot(driver, "box_page_error")
        allure.attach.file(screenshot_path, name="Box Error", attachment_type=allure.attachment_type.PNG)
        raise e