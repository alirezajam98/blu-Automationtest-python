import json
import allure
import pytest
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


@allure.epic("Dashboard")
@allure.feature("Dashboard Page Verification")
@allure.story("Verify all text elements and buttons on Dashboard page")
# Suites
@allure.suite(f"Version:{VERSION}")
@allure.sub_suite("Text Verification for Dashboard Page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_dashboard_page(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard
    text_reference = load_text_reference()
    dashboard_texts = text_reference["dashboard_page"]

    try:
        with allure.step("Navigate to Dashboard Tab"):
            logger.info("ورود به تب داشبورد...")
            dashboard_page.dashboard_tab_button()
            logger.info("وارد تب داشبورد شد.")

        with allure.step("Verify Balance Text"):
            logger.info("بررسی متن موجودی حساب...")
            check_text_match(
                dashboard_page.get_balance_text(),
                dashboard_texts["balance_text"],
                "متن موجودی حساب"
            )

        with allure.step("Verify Charge Button Text"):
            logger.info("بررسی متن دکمه شارژ حساب...")
            check_text_match(
                dashboard_page.get_charge_button_text(),
                dashboard_texts["charge_button_text"],
                "متن دکمه شارژ حساب"
            )

        with allure.step("Verify Box Button Text"):
            logger.info("بررسی متن دکمه باکس...")
            check_text_match(
                dashboard_page.get_box_button_text(),
                dashboard_texts["box_button_text"],
                "متن دکمه باکس"
            )

        with allure.step("Verify Analytics Button Text"):
            logger.info("بررسی متن دکمه گزارش مالی...")
            check_text_match(
                dashboard_page.get_analytics_button_text(),
                dashboard_texts["analytics_button_text"],
                "متن دکمه گزارش مالی"
            )

        with allure.step("Verify No Transaction Text"):
            logger.info("بررسی متن 'تراکنشی ندارید'...")
            check_text_match(
                dashboard_page.get_no_transaction_text(),
                dashboard_texts["no_transaction_text"],
                "متن 'تراکنشی ندارید'"
            )

        with allure.step("Verify No Transaction Description"):
            logger.info("بررسی متن توضیحات 'اولین تراکنش خود را انجام دهید'...")
            check_text_match(
                dashboard_page.get_no_transaction_description(),
                dashboard_texts["no_transaction_description"],
                "متن توضیحات 'اولین تراکنش خود را انجام دهید'"
            )

    except Exception as e:
        logger.error(f"خطا در بررسی صفحه داشبورد: {e}")
        screenshot_path = capture_screenshot(driver, "dashboard_page_error")
        allure.attach.file(screenshot_path, name="Dashboard Error", attachment_type=allure.attachment_type.PNG)
        raise e
