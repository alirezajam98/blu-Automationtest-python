import allure

from pages.card.card_first_order_pages import CardFirstOrderPages
from utils.config import capture_screenshot
from utils.utils import logger
from pages.kyc.kyc_pages import CreateAccountConfirmPage
from utils.utils import remove_used_account


def test_card_first_order(login_and_dashboard_with_confirmed_user):
    driver, username = login_and_dashboard_with_confirmed_user  # دریافت یوزر نیم از فیکسچر
    try:
        with allure.step("Click on card order button"):
            logger.info("کلیک روی دکمه شروع سفارش کارت...")
            card_first_order_page = CardFirstOrderPages(driver)
            card_first_order_page.start_card_order_button()
            logger.info("روی دکمه سفارش کارت کلیک شد!")
        with allure.step("click on accept button for "):
            card_first_order_page.start_card_order_button()

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        screenshot_path = capture_screenshot(driver, "dynamic_pin_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e

    # حذف یوزر در صورت موفقیت‌آمیز بودن تست
    try:
        remove_used_account(username)
        logger.info(f"User '{username}' removed from confirmed accounts after successful test.")
    except Exception as e:
        logger.error(f"Failed to remove user '{username}': {e}")
