import allure
import pytest

from pages.hub.charge.charge_pages import ChargePages
from pages.transfer.transfer_page import TransferPage
from utils.config import configure_logger, capture_screenshot
from utils.utils import check_text_match

# تنظیمات لاگ
logger = configure_logger()


@allure.epic("Hub")
@allure.feature("Charge Irancell Flow")
@allure.story("Verify Irancell charge flow")
@pytest.mark.parametrize("login_and_dashboard", ["andauto1"], indirect=True)
def test_charge_irancell_flow(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard
    charge_pages = ChargePages(driver)
    try:
        with allure.step("Navigate to hub Tab"):
            logger.info("ورود به تب فروشگاه...")
            dashboard_page.hub_tab_button()
            logger.info("وارد تب فروشگاه شد.")

        with allure.step("Click on 'Charge' option"):
            logger.info("کلیک روی گزینه 'شارژ'...")
            charge_pages.click_charge_option()
            logger.info("گزینه 'شارژ' کلیک شد.")

        with allure.step("Verify Page Title"):
            logger.info("بررسی عنوان صفحه...")
            check_text_match(
                charge_pages.get_page_title_text(),
                "شارژ",
                "عنوان صفحه"
            )

        with allure.step("Enter Phone Number"):
            logger.info("وارد کردن شماره تلفن...")
            charge_pages.enter_phone_number("09031034233")
            logger.info("شماره تلفن وارد شد.")

        with allure.step("Click Confirm Button"):
            logger.info("کلیک روی دکمه 'تایید'...")
            charge_pages.click_confirm_button()
            logger.info("دکمه 'تایید' کلیک شد.")

        with allure.step("Select Irancell Operator"):
            logger.info("انتخاب اپراتور 'ایرانسل'...")
            charge_pages.select_operator("ایرانسل")
            logger.info("اپراتور 'ایرانسل' انتخاب شد.")

        with allure.step("Select Charge Amount"):
            logger.info("انتخاب مبلغ شارژ...")
            charge_pages.select_charge_amount("۲۰٬۰۰۰ ریال")
            logger.info("مبلغ شارژ انتخاب شد.")

        with allure.step("Click Payment Button"):
            logger.info("کلیک روی دکمه 'پرداخت'...")
            charge_pages.click_payment_button()
            logger.info("دکمه 'پرداخت' کلیک شد.")

        with allure.step("Verify Top Title"):
            logger.info("بررسی عنوان بالای صفحه...")
            check_text_match(
                charge_pages.get_top_title_text(),
                "شارژ ایرانسل",
                "عنوان بالای صفحه"
            )

        with allure.step("Click Accept Button"):
            logger.info("کلیک روی دکمه 'قبول'...")
            charge_pages.click_accept_button()
            logger.info("دکمه 'قبول' کلیک شد.")

        with allure.step("Verify Transfer Status"):
            logger.info("بررسی وضعیت انتقال...")
            check_text_match(
                charge_pages.get_transfer_status(),
                "موفق",
                "وضعیت انتقال"
            )

    except Exception as e:
        logger.error(f"خطا در فرآیند خرید شارژ ایرانسل: {e}")
        screenshot_path = capture_screenshot(driver, "charge_irancell_error")
        allure.attach.file(screenshot_path, name="Charge Irancell Error", attachment_type=allure.attachment_type.PNG)
        raise e