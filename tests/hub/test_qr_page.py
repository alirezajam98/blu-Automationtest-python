import json
import allure
import pytest
from pages.hub.hub_page import HubPage
from pages.hub.qr_page import QrPage, MyQrPage, AddPricePage
from pages.permissions_dialog import PermissionsDialog
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
@allure.feature("QR Page")
@allure.story("Verify all displayed texts on QR Page")
# Suites
@allure.suite(f"Version:{VERSION}")
@allure.sub_suite("Text Verification for QR Page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_qr_page(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard
    text_reference = load_text_reference()
    qr_texts = text_reference["qr_page"]
    qr_page = QrPage(driver)
    hub_page = HubPage(driver)
    try:
        with allure.step("Navigate to Hub Page"):
            logger.info("ورود به صفحه هاب...")
            dashboard_page.hub_tab_button()
            logger.info("وارد صفحه هاب شد.")

        with allure.step("Scroll to open QR page"):
            logger.info("اسکرول برای باز کردن صفحه اسکن...")
            hub_page.scroll()
            logger.info("وارد صفحه اسکن شد.")

        with allure.step("Click on Allow button for camera permission"):
            logger.info("کلیک روی تایید دسترسی این بخش به دوربین...")
            permissions_dialog = PermissionsDialog(driver)
            permissions_dialog.allow_camera_permission()
            logger.info("روی تایید دسترسی دوربین کلیک شد.")

        with allure.step("Verify title Text"):
            check_text_match(
                qr_page.get_page_title(),
                qr_texts["page_title"],
                "متن صفحه qr"
            )

        with allure.step("Verify My QR Text"):
            check_text_match(
                qr_page.open_my_qr_title(),
                qr_texts["my_qr"],
                "متن دکمه کد qr من"
            )

        with allure.step("Click on Flash on"):
            logger.info("روشن کردن فلش...")
            qr_page.toggle_flash()
            logger.info("فلش روشن شد.")

        with allure.step("Click on Flash off"):
            logger.info("خاموش کردن فلش...")
            qr_page.toggle_flash()
            logger.info("فلش خاموش شد.")

        with allure.step("Click on My QR Code Button"):
            logger.info("کلیک روی دکمه کد من...")
            qr_page.open_my_qr()
            logger.info("صفحه کد QR من باز شد.")

        with allure.step("Verify My QR Text Title Page"):
            my_qr_page = MyQrPage(driver)
            check_text_match(
                my_qr_page.get_title_my_qr_page(),
                qr_texts["my_qr_title"],
                "متن توضیح صفحه کد qr من"
            )

        with allure.step("Verify Add Price Text"):
            check_text_match(
                my_qr_page.get_add_price_title(),
                qr_texts["add_price"],
                "متن افزودن میلغ"
            )

        with allure.step("Verify Share Text"):
            check_text_match(
                my_qr_page.get_share_title(),
                qr_texts["share"],
                "متن ارسال/ذخیره"
            )

        with allure.step("Click on Add Price Button"):
            logger.info("کلیک روی دکمه افزودن مبلغ...")
            my_qr_page.click_amount()
            logger.info("صفحه افزودن مبلغ باز شد.")

        with allure.step("Verify Price Page Title"):
            add_price_page = AddPricePage(driver)
            check_text_match(
                add_price_page.get_page_title(),
                qr_texts["add_price_page_title"],
                "متن مبلغ کد QR"
            )

        with allure.step("Verify Price Field Title"):
            check_text_match(
                add_price_page.get_add_price_title(),
                qr_texts["title_filed_amount"],
                "متن توضیح فیلد مبلغ"
            )

        with allure.step("Verify Price Field Text"):
            check_text_match(
                add_price_page.get_amount_field_text(),
                qr_texts["field_text"],
                "متن فیلد مبلغ"
            )

        with allure.step("Input Amount In Field"):
            logger.info("وارد کردن مبلغ در فیلد مبلغ...")
            add_price_page.input_amount("200000")
            logger.info("مبلغ '200000' در فیلد وارد شد.")

        with allure.step("Click on Save"):
            logger.info("کلیک روی دکمه ذخیره...")
            add_price_page.click_save_button_title()
            logger.info("روی دکمه ذخیره کلیک شد.")


        with allure.step("Verify My QR Text Title Page"):
            my_qr_page = MyQrPage(driver)
            check_text_match(
                my_qr_page.get_toast_text(),
                qr_texts["toast"],
                "متن تست انجام شدن"
            )

    except Exception as e:
        logger.error(f"خطا در بررسی متن‌های  صفحه اسکن: {e}")
        screenshot_path = capture_screenshot(driver, "QR_page_verification_error")
        allure.attach.file(screenshot_path, name="QR Page Error", attachment_type=allure.attachment_type.PNG)
        raise e
