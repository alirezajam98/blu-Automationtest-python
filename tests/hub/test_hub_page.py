import json
import allure
import pytest
from pages.hub.hub_page import HubPage
from utils.config import configure_logger, capture_screenshot
from utils.utils import check_text_match

# تنظیمات لاگ
logger = configure_logger()


# تابعی برای بارگذاری فایل JSON
def load_text_reference():
    with open('utils/text_reference.json', 'r', encoding='utf-8') as f:
        return json.load(f)


with open('utils/version.json') as f:
    config = json.load(f)
    VERSION = config.get("version", "unknown_version")


@allure.epic("Hub")
@allure.feature("Hub Page")
@allure.story("Verify all displayed texts on Hub Page")
# Suites
@allure.suite(f"Version:{VERSION}")
@allure.sub_suite("Text Verification for Hub Page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_hub_page_texts(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard
    text_reference = load_text_reference()
    hub_texts = text_reference["hub_page"]
    hub_page = HubPage(driver)

    try:
        with allure.step("Navigate to Hub Page"):
            logger.info("ورود به صفحه هاب...")
            dashboard_page.hub_tab_button()
            logger.info("وارد صفحه هاب شد.")

        # بررسی متن‌های اصلی
        with allure.step("Verify QR Title Text"):
            check_text_match(
                hub_page.get_qr_title_text(),
                hub_texts["qr_title"],
                "عنوان QR"
            )

        with allure.step("Verify Charge Text"):
            check_text_match(
                hub_page.get_charge_text(),
                hub_texts["charge_text"],
                "متن گزینه شارژ"
            )

        with allure.step("Verify Internet Text"):
            check_text_match(
                hub_page.get_internet_text(),
                hub_texts["internet_text"],
                "متن گزینه اینترنت"
            )

        with allure.step("Verify Bill Text"):
            check_text_match(
                hub_page.get_bill_text(),
                hub_texts["bill_text"],
                "متن گزینه قبض"
            )

        with allure.step("Verify Refund Text"):
            check_text_match(
                hub_page.get_refund_text(),
                hub_texts["refund_text"],
                "متن گزینه برگشت پول"
            )

        with allure.step("Verify loan Text"):
            check_text_match(
                hub_page.get_loan_text(),
                hub_texts["loan_text"],
                "متن گزینه وام"
            )

        with allure.step("Verify check Text"):
            check_text_match(
                hub_page.get_check_text(),
                hub_texts["check_text"],
                "متن گزینه چک"
            )

        with allure.step("Verify dong Text"):
            check_text_match(
                hub_page.get_dong_text(),
                hub_texts["dong_text"],
                "متن گزینه دنگ"
            )

        with allure.step("Verify auto payment Text"):
            check_text_match(
                hub_page.get_auto_payment_text(),
                hub_texts["auto_payment_text"],
                "متن گزینه پرداخت خودکار"
            )

        with allure.step("Verify car services Text"):
            check_text_match(
                hub_page.get_car_services_text(),
                hub_texts["car_services_text"],
                "متن گزینه خدمات خودرو"
            )

        with allure.step("Verify invite friends Text"):
            check_text_match(
                hub_page.get_invite_friends_text(),
                hub_texts["invite_friends_text"],
                "متن گزینه دعوت دوستان"
            )

        with allure.step("Verify junior Text"):
            check_text_match(
                hub_page.get_junior_text(),
                hub_texts["junior_text"],
                "متن گزینه جونیور"
            )


    except Exception as e:
        logger.error(f"خطا در بررسی متن‌های هاب: {e}")
        screenshot_path = capture_screenshot(driver, "hub_text_verification_error")
        allure.attach.file(screenshot_path, name="Hub Error", attachment_type=allure.attachment_type.PNG)
        raise e
