import json
import allure
import pytest

from pages.dashboard.box.box_page import BoxPage
from pages.dashboard.box.box_profile_page import BoxProfilePage
from pages.dashboard.box.select_box_name_page import CreateBoxPage
from pages.dashboard.box.select_box_type_page import SelectBoxTypePage
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
@allure.story("Select Box Type and Create Box")
@allure.suite(f"Version:{VERSION}")
@allure.sub_suite("Box Type Selection and Creation")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_select_box_type_page(login_and_dashboard):
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

        with allure.step("Click on 'New Box' button (BLOCKER)"):
            logger.info("کلیک روی دکمه 'باکس جدید'...")
            box_page.click_new_box()

        with allure.step("Check normal box title and description"):
            logger.info("بررسی عنوان و توضیحات باکس عادی...")
            select_box_type_page = SelectBoxTypePage(driver)
            check_text_match(
                select_box_type_page.get_normal_box_title(),
                box_texts["normal_box_title"],
                "عنوان 'بلوباکس'"
            )
            check_text_match(
                select_box_type_page.get_normal_box_description(),
                box_texts["normal_box_description"],
                "توضیح 'بلوباکس'"
            )

        with allure.step("Check long term box title and description"):
            logger.info("بررسی عنوان و توضیحات باکس بلند مدت...")
            check_text_match(
                select_box_type_page.get_long_term_box_title(),
                box_texts["long_term_box_title"],
                "عنوان 'بیگ‌باکس'"
            )
            check_text_match(
                select_box_type_page.get_long_term_box_description(),
                box_texts["long_term_box_description"],
                "توضیح 'بیگ‌باکس'"
            )

        with allure.step("Select normal box"):
            logger.info("انتخاب باکس عادی (بلوباکس)...")
            select_box_type_page.select_normal_box()

        with allure.step("Enter box name and save"):
            logger.info("ورود نام باکس و ذخیره...")
            create_box_page = CreateBoxPage(driver)
            create_box_page.close_keyboard()
            create_box_page.enter_box_name("My Test Box1")
            create_box_page.save_new_box()

        with allure.step("Check if the box profile page is displayed"):
            box_profile_page = BoxProfilePage(driver)
            check_text_match(
                box_profile_page.get_deposit_btn_text(),
                box_texts["deposit_button_text"],
                "متن دکمه واریز"
            )
            logger.info("باکس با موفقیت ایجاد شد.")

    except Exception as e:
        logger.error(f"خطا در تست انتخاب نوع باکس و ایجاد باکس: {e}")
        screenshot_path = capture_screenshot(driver, "select_box_type_error")
        allure.attach.file(screenshot_path, name="Select Box Type Error", attachment_type=allure.attachment_type.PNG)
        raise e
