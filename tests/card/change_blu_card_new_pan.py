import json
import allure
import pytest
from pages.card.card_page import CardPage
from pages.card.card_security_setting_page import CardSecuritySettingsPages
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

@allure.epic("Card Management")
@allure.feature("Change First Password (PIN1)")
@allure.story("Allow users to change their first password (PIN1)")
# Suites
@allure.suite(f"version:{VERSION}")
@allure.sub_suite("Tests for Changing First Password (PIN1)")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://jira.sdb247.com/browse/QA-22103", name="Jira Task")
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_change_blu_card_new_pan(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard

    # بارگذاری فایل JSON
    text_reference = load_text_reference()

    try:
        with allure.step("Navigate to Card Tab"):
            logger.info("ورود به تب کارت...")
            dashboard_page.card_tab_button()
            logger.info("وارد تب کارت شد.")

        with allure.step("Verify 'Change Blu Card' Button Text"):
            logger.info("بررسی متن دکمه تعویض بلو کارت...")
            card_page = CardPage(driver)
            check_text_match(
                card_page.change_blu_card_button_title(),
                text_reference["card_page"]["change_blu_card_button_title"],
                "متن دکمه تعویض بلو کارت"
            )
    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        screenshot_path = capture_screenshot(driver, "change_pin1_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
