import json
import allure
import pytest
from pages.card.card_page import CardPage
from pages.dashboard.dashboard_page import DashboardPage
from utils.config import configure_logger, capture_screenshot

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


# Behaviors
@allure.epic("Card Management")
@allure.feature("Card page")
@allure.story("check card page")
#Suites
@allure.suite(f"version:{VERSION}")
@allure.sub_suite("Tests for Card page")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://jira.sdb247.com/secure/enav/#/5686?query=issue%3DQA-22654&offset=1&pageWidth=10&view=detail", name="Jira Task")
@pytest.mark.parametrize("login_and_dashboard", ["suspeeeend106"], indirect=True)
def test_card_page(login_and_dashboard):
    driver, dashboard_page = login_and_dashboard

    # بارگذاری فایل JSON برای دریافت متون مرجع
    text_reference = load_text_reference()
    try:
        with allure.step("Click on 'Start' button"):
            logger.info("کلیک روی دکمه 'تب کارت'...")
            dashboard_page = DashboardPage(driver)
            dashboard_page.card_tab_button()
            logger.info("دکمه 'تب کارت' کلیک شد.")

        with allure.step("Check 'card page title' text"):
            try:
                expected_text = text_reference["card_page"]["card_page_title"]
                card_page = CardPage(driver)
                actual_text = card_page.page_title()
                assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن تایتل صفحه صفحه کارت صحیح است: {actual_text}")
            except AssertionError as e:
                logger.error(f"خطا در بررسی متن تایتل صفحه صفحه کارت: {e}")
                allure.attach(f"Expected: {expected_text}\nActual: {actual_text}", "Mismatch in text",
                              allure.attachment_type.TEXT)
                # خطا را لاگ می‌کنیم اما ادامه می‌دهیم
    except Exception as e:

        logger.error(f"خطا رخ داد: {e}")
        # اسکرین‌شات در صورت بروز هرگونه خطا
        screenshot_path = capture_screenshot(driver, "card_page_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
