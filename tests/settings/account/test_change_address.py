import json
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from pages.setting.account.account_page import AccountPage
from pages.setting.account.change_address_page import ChangeAddressPage, EditAddressPage
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


@allure.epic("Profile")  # کلی‌ترین دسته‌بندی
@allure.feature("Account Page")  # زیرمجموعه مدیریت حساب
@allure.story("Change Address")  # داستان کاربری خاص تغییر آدرس
@allure.suite(f"Version: {VERSION}")  # اطلاعات دستگاه
@allure.sub_suite("Address Management")  # زیرمجموعه مدیریت آدرس
@allure.severity(allure.severity_level.CRITICAL)  # سطح اهمیت
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_change_address(login_and_dashboard):
    # ... باقی کد تست
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

        # کلیک روی گزینه تغییر آدرس محل سکونت
        with allure.step("Navigate to Change Address Page"):
            logger.info("کلیک روی گزینه تغییر آدرس محل سکونت...")
            account_page.click_change_address_option()

        # ایجاد شیء صفحه تغییر آدرس
        change_address_page = ChangeAddressPage(driver)

        # بررسی عنوان صفحه تغییر آدرس
        with allure.step("Verify Change Address Page Title"):
            logger.info("بررسی عنوان صفحه تغییر آدرس...")
            check_text_match(
                change_address_page.get_page_title(),
                text_reference["change_address_page"]["title"],
                "عنوان صفحه تغییر آدرس"
            )

        # بررسی متن راهنمای فیلد ورودی کدپستی
        with allure.step("Verify Postal Code Input Hint"):
            logger.info("بررسی متن راهنمای فیلد ورودی کدپستی...")
            check_text_match(
                change_address_page.get_input_hint(),
                text_reference["change_address_page"]["input_hint"],
                "متن راهنمای فیلد ورودی کدپستی"
            )

        # وارد کردن کدپستی
        with allure.step("Enter Postal Code"):
            logger.info("وارد کردن کدپستی...")
            change_address_page.enter_postal_code("1563653417")

        # بررسی فعال بودن دکمه ادامه
        with allure.step("Verify Continue Button State"):
            logger.info("بررسی فعال بودن دکمه ادامه...")
            assert change_address_page.is_continue_button_enabled(), "دکمه ادامه غیرفعال است."

        # کلیک روی دکمه ادامه
        with allure.step("Click Continue Button"):
            logger.info("کلیک روی دکمه ادامه...")
            change_address_page.click_continue_button()

        with allure.step("Perform Swipe Gesture"):
            logger.info("اجرای ژست سوایپ روی صفحه...")
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            # موقعیت شروع سوایپ (مثلاً نقطه‌ای در صفحه)
            actions.w3c_actions.pointer_action.move_to_location(1095, 1877)
            actions.w3c_actions.pointer_action.pointer_down()
            # حرکت به سمت نقطه نهایی سوایپ
            actions.w3c_actions.pointer_action.move_to_location(548, 1723)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            # موقعیت شروع سوایپ (مثلاً نقطه‌ای در صفحه)
            actions.w3c_actions.pointer_action.move_to_location(1095, 1877)
            actions.w3c_actions.pointer_action.pointer_down()
            # حرکت به سمت نقطه نهایی سوایپ
            actions.w3c_actions.pointer_action.move_to_location(548, 1723)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            logger.info("ژست سوایپ با موفقیت انجام شد.")

        with allure.step("Click Continue Button"):
            logger.info("کلیک روی دکمه ادامه...")
            change_address_page.click_continue_button_in_map()

        edit_address_page = EditAddressPage(driver)

        # بررسی مقادیر نمایشی
        with allure.step("Verify Displayed Address Values"):
            check_text_match(
                edit_address_page.get_province_city_value(),
                text_reference["edit_address_page"]["province_city"],
                "استان و شهر"
            )

            check_text_match(
                edit_address_page.get_street_value(),
                text_reference["edit_address_page"]["street"],
                "خیابان اصلی"
            )

            check_text_match(
                edit_address_page.get_avenue_value(),
                text_reference["edit_address_page"]["avenue"],
                "خیابان فرعی"
            )

        # ویرایش تنها فیلد قابل ویرایش
        with allure.step("Edit Unit Information"):
            edit_address_page.enter_unit("طبقه ۵، واحد ۱")

        # بررسی فعال بودن دکمه
        with allure.step("Verify Confirm Button State"):
            assert edit_address_page.is_confirm_button_enabled(), "دکمه تأیید غیرفعال است"

        # کلیک روی دکمه تأیید
        with allure.step("Confirm Changes"):
            edit_address_page.click_confirm_button()


    except Exception as e:
        capture_screenshot(driver, "change_address_verification")
        logger.error(f"خطا در فرآیند تغییر آدرس: {str(e)}")
        raise
