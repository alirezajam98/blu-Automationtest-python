import json

import allure
import pytest

from pages.dashboard.box.box_confirm_modal import BoxConfirmModal
from pages.dashboard.box.box_page import BoxPage
from pages.dashboard.box.box_profile_page import BoxProfilePage
from pages.dashboard.box.box_setting_bottom_sheet import BoxSettingBottomSheet
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
@allure.feature("Box Settings")
@allure.story("Edit Box Name and Delete Box")
@allure.suite(f"Version:{VERSION}")
@allure.sub_suite("Box Settings Management")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_edit_box_name_and_delete_box(login_and_dashboard):
    """تست ویرایش نام باکس و حذف باکس با تأیید و کنسل"""
    driver, dashboard_page = login_and_dashboard
    text_reference = load_text_reference()
    box_texts = text_reference["box_page"]
    box_page = BoxPage(driver)
    box_profile_page = BoxProfilePage(driver)
    try:
        with allure.step("Navigate to Box Tab"):
            logger.info("ورود به تب باکس...")
            dashboard_page.click_box_button()
            logger.info("وارد تب باکس شد.")

        with allure.step("Close the onboarding page"):
            logger.info("بستن صفحه انبوردینگ...")
            box_page.close_onboarding()
            logger.info("صفحه انبوردینگ بسته شد.")

        with allure.step("Check if first box name is correct"):
            check_text_match(
                box_page.get_first_box_name(),
                box_texts["first_box_name"],
                "نام اولین باکس"
            )

        with allure.step("Check if first box amount is correct"):
            check_text_match(
                box_page.get_first_box_amount(),
                box_texts["first_box_amount"],
                "مقدار اولین باکس"
            )

        with allure.step("Click on the first box and navigate to profile"):
            logger.info("کلیک روی اولین باکس و هدایت به صفحه پروفایل باکس...")
            box_page.click_first_box()
            logger.info("صفحه پروفایل باکس نمایش داده شد.")

        with allure.step("Click on setting button and open settings bottom sheet"):
            logger.info("باز کردن تنظیمات باکس...")
            box_profile_page.click_box_settings()
            logger.info("صفحه تنظیمات باکس نمایش داده شد.")

        with allure.step("Click on 'Delete Box' and open confirmation modal"):
            logger.info("کلیک روی 'حذف باکس'...")
            box_setting_bottom_sheet = BoxSettingBottomSheet(driver)
            box_setting_bottom_sheet.click_delete_box()

        with allure.step("Cancel deletion and return to box profile"):
            logger.info("کنسل کردن حذف...")
            confirm_modal = BoxConfirmModal(driver)
            confirm_modal.cancel_delete()

        with allure.step("Click on setting button and open settings bottom sheet"):
            logger.info("باز کردن تنظیمات باکس...")
            box_profile_page.click_box_settings()

        with allure.step("Click on 'Delete Box' and open confirmation modal"):
            logger.info("کلیک روی 'حذف باکس'...")
            box_setting_bottom_sheet.click_delete_box()

        with allure.step("Confirm deletion and return to box page"):
            logger.info("تایید کردن حذف...")
            confirm_modal.confirm_delete()

        with allure.step("Check 'باکس فعالی ندارید' text"):
            check_text_match(
                box_page.get_no_active_box_title(),
                box_texts["no_active_box_title"],
                "متن 'باکس فعالی ندارید'"
            )

        with allure.step("Check '۰ ریال' text"):
            check_text_match(
                box_page.get_box_deposit_text(),
                box_texts["box_deposit_text"],
                "متن '۰ ریال'"
            )

        with allure.step("Check 'موجودی باکس‌ها' text"):
            check_text_match(
                box_page.get_box_deposit_description(),
                box_texts["box_deposit_description"],
                "متن 'موجودی باکس‌ها'"
            )

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        screenshot_path = capture_screenshot(driver, "edit_box_name_and_delete_box_error")
        allure.attach.file(screenshot_path, name="Edit Box Name and Delete Box Error",
                           attachment_type=allure.attachment_type.PNG)
        raise e
