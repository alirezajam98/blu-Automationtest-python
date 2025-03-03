import json
import allure
import pytest
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


@allure.epic("Profile")
@allure.feature("Settings Page")
@allure.story("Verify all displayed texts on Settings Page")
# Suites
@allure.suite(f"Version:{VERSION}")
@allure.sub_suite("Text Verification for Settings Page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_verify_settings_texts(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard

    # بارگذاری فایل JSON
    text_reference = load_text_reference()

    try:
        with allure.step("Navigate to Settings Tab"):
            logger.info("ورود به تب تنظیمات...")
            dashboard_page.click_settings_button()
            logger.info("وارد تب تنظیمات شد.")

        settings_page = SettingPage(driver)

        # بررسی متن‌ها به ترتیب مشخص‌شده
        with allure.step("Verify 'User Account' Text"):
            logger.info("بررسی متن گزینه حساب کاربری...")
            check_text_match(
                settings_page.get_user_account_text(),
                text_reference["settings_page"]["user_account"],
                "متن گزینه حساب کاربری"
            )

        with allure.step("Verify 'Security and Privacy' Text"):
            logger.info("بررسی متن گزینه امنیت و حریم خصوصی...")
            check_text_match(
                settings_page.get_security_and_privacy_text(),
                text_reference["settings_page"]["security_and_privacy"],
                "متن گزینه امنیت و حریم خصوصی"
            )

        with allure.step("Verify 'Notifications' Text"):
            logger.info("بررسی متن گزینه اطلاع‌رسانی...")
            check_text_match(
                settings_page.get_notifications_text(),
                text_reference["settings_page"]["notifications"],
                "متن گزینه اطلاع‌رسانی"
            )
            check_text_match(
                settings_page.get_notifications_subtext(),
                text_reference["settings_page"]["notifications_subtext"],
                "متن فرعی اطلاع‌رسانی"
            )

        with allure.step("Verify 'Display Blu' Text"):
            logger.info("بررسی متن گزینه نمایش بلو...")
            check_text_match(
                settings_page.get_display_blu_text(),
                text_reference["settings_page"]["display_blu"],
                "متن گزینه نمایش بلو"
            )
            check_text_match(
                settings_page.get_display_blu_subtext(),
                text_reference["settings_page"]["display_blu_subtext"],
                "متن فرعی نمایش بلو"
            )

        with allure.step("Verify 'Update' Text"):
            logger.info("بررسی متن گزینه به‌روزرسانی...")
            check_text_match(
                settings_page.get_update_text(),
                text_reference["settings_page"]["update"],
                "متن گزینه به‌روزرسانی"
            )
            check_text_match(
                settings_page.get_update_subtext(),
                text_reference["settings_page"]["update_subtext"],
                "متن فرعی به‌روزرسانی"
            )

        with allure.step("Verify 'Blu Club' Text"):
            logger.info("بررسی متن گزینه بلوکلاب...")
            check_text_match(
                settings_page.get_blu_club_text(),
                text_reference["settings_page"]["blu_club"],
                "متن گزینه بلوکلاب"
            )
            check_text_match(
                settings_page.get_blu_club_subtext(),
                text_reference["settings_page"]["blu_club_subtext"],
                "متن فرعی بلوکلاب"
            )

        with allure.step("Verify 'Support' Text"):
            logger.info("بررسی متن گزینه پشتیبانی...")
            check_text_match(
                settings_page.get_support_text(),
                text_reference["settings_page"]["support"],
                "متن گزینه پشتیبانی"
            )
            check_text_match(
                settings_page.get_support_subtext(),
                text_reference["settings_page"]["support_subtext"],
                "متن فرعی پشتیبانی"
            )

        with allure.step("Verify 'Invite Friends' Text"):
            logger.info("بررسی متن گزینه دعوت دوستان...")
            check_text_match(
                settings_page.get_invite_friends_text(),
                text_reference["settings_page"]["invite_friends"],
                "متن گزینه دعوت دوستان"
            )
            check_text_match(
                settings_page.get_invite_friends_subtext(),
                text_reference["settings_page"]["invite_friends_subtext"],
                "متن فرعی دعوت دوستان"
            )

        with allure.step("Verify 'Feedback' Text"):
            logger.info("بررسی متن گزینه ثبت ایده‌ها و نظرات...")
            check_text_match(
                settings_page.get_feedback_text(),
                text_reference["settings_page"]["feedback"],
                "متن گزینه ثبت ایده‌ها و نظرات"
            )
            check_text_match(
                settings_page.get_feedback_subtext(),
                text_reference["settings_page"]["feedback_subtext"],
                "متن فرعی ثبت ایده‌ها و نظرات"
            )

        with allure.step("Verify 'Blu' Text"):
            logger.info("بررسی متن گزینه بلو...")
            check_text_match(
                settings_page.get_blu_text(),
                text_reference["settings_page"]["blu"],
                "متن گزینه بلو"
            )
            check_text_match(
                settings_page.get_blu_subtext(),
                text_reference["settings_page"]["blu_subtext"],
                "متن فرعی بلو"
            )

        with allure.step("Verify 'Version' Text"):
            logger.info("بررسی متن نسخه برنامه...")
            check_text_match(
                settings_page.get_version_text(),
                text_reference["settings_page"]["version"],
                "متن نسخه برنامه"
            )

        with allure.step("Verify 'Made In' Text"):
            logger.info("بررسی متن Made In...")
            check_text_match(
                settings_page.get_made_in_text(),
                text_reference["settings_page"]["made_in"],
                "متن Made In"
            )

        logger.info("تمامی متن‌های صفحه تنظیمات بررسی شدند.")

    except Exception as e:
        capture_screenshot(driver, "settings_page_text_verification")
        logger.error(f"خطا هنگام بررسی متن‌های صفحه تنظیمات: {str(e)}")
        raise
