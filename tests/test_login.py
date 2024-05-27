import pytest
import yaml
import logging
import os

from pages.HomePage import HomePage
from pages.Login.Login_page import LoginPage
from pages.Login.Notif_BottomSheet import Notif_BottomSheet
from utils.driver import create_driver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# تنظیم لاگر برای ثبت لاگ‌ها در فایل 'test_log.log'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("test_log.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# تابع برای بارگذاری تنظیمات از فایل YAML
def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config


config = load_config()


# تابع برای گرفتن اسکرین‌شات و ذخیره آن در پوشه 'screenshots'
def take_screenshot(driver, name):
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    screenshot_path = os.path.join('screenshots', f"{name}.png")
    driver.save_screenshot(screenshot_path)
    logger.info(f"Screenshot saved to {screenshot_path}")


@pytest.mark.parametrize("device_name", config['desired_caps'].keys())
def test_login_with_biometric(device_name, caplog):
    with caplog.at_level(logging.INFO):
        logger.info(f"Running test on device: {device_name}")
        desired_caps = config['desired_caps'][device_name]
        driver = create_driver(device_name)

        try:
            # مرحله ورود یوزرنیم و پسورد
            login_page = LoginPage(driver)
            login_page.enter_username('aljm')
            login_page.enter_password('Bb123456')
            logger.info(f"Entered username and password on device: {device_name}")

            # کلیک روی دکمه لاگین
            biometric_page = login_page.press_login_button()
            logger.info(f"Clicked on login button on device: {device_name}")

            # اعتبارسنجی ورود به صفحه بومتریک
            assert biometric_page.is_btn_not_now_displayed(), "Biometric page should be displayed after login"
            logger.info(f"Biometric page displayed after login on device: {device_name}")

        except (NoSuchElementException, TimeoutException, AssertionError) as e:
            # ثبت خطا، گرفتن اسکرین‌شات و fail کردن تست در صورت بروز خطا
            logger.error(f"Error during login steps on device: {device_name} - {str(e)}")
            take_screenshot(driver, f"login_error_{device_name}")
            driver.quit()  # بستن درایور
            pytest.fail(f"Test failed during login steps on device: {device_name}")

        try:
            # کلیک روی دکمه "Not Now" در صفحه بومتریک
            biometric_page.click_btn_not_now()
            logger.info(f"Clicked on 'Not Now' button on device: {device_name}")

            # بررسی وجود دکمه اجازه دسترسی به نوتیفیکیشن و کلیک در صورت وجود
            notif_BottomSheet = Notif_BottomSheet(driver)
            if notif_BottomSheet.is_permission_button_displayed():
                notif_BottomSheet.click_Permission_button()
                logger.info(f"Clicked on permission button on device: {device_name}")

            # اعتبارسنجی نتیجه لاگین
            home_page = HomePage(driver)
            assert home_page.get_welcome_message() == "خانه"
            logger.info(f"Verified welcome message on device: {device_name}")

        except (NoSuchElementException, TimeoutException, AssertionError) as e:
            # ثبت خطا و گرفتن اسکرین‌شات در صورت بروز خطا در مراحل بعدی
            logger.error(f"Error during subsequent steps on device: {device_name} - {str(e)}")
            take_screenshot(driver, f"subsequent_steps_error_{device_name}")

        finally:
            # بستن درایور پس از اتمام تست
            driver.quit()
            logger.info(f"Test completed on device: {device_name}")

