import pytest
import yaml

from pages.HomePage import HomePage
from pages.Login.Login_page import LoginPage
from pages.Login.Notif_BottomSheet import Notif_BottomSheet
from utils.driver import create_driver
from selenium.common.exceptions import NoSuchElementException


def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config


config = load_config()


@pytest.mark.parametrize("device_name", config['desired_caps'].keys())
def test_login_with_biometric(device_name):
    desired_caps = config['desired_caps'][device_name]
    # ایجاد درایور با تنظیمات مربوط به دستگاه مورد نظر
    driver = create_driver(device_name)

    login_page = LoginPage(driver)

    # وارد کردن یوزرنیم و پسورد
    login_page.enter_username('aljm')
    login_page.enter_password('Bb123456')
    print("Entered username and password")

    # کلیک بر روی دکمه لاگین
    biometric_page = login_page.press_login_button()
    print("Clicked on login button")

    # اعتبارسنجی ورود به صفحه بومتریک
    assert biometric_page.is_btn_not_now_displayed(), "Biometric page should be displayed after login"
    print("Biometric page displayed after login")

    # کلیک بر روی دکمه "Not Now" در صفحه بومتریک
    biometric_page.click_btn_not_now()
    print("Clicked on 'Not Now' button")

    # بررسی وجود دکمه اجازه دسترسی به نوتیفیکیشن و کلیک در صورت وجود
    notif_BottomSheet = Notif_BottomSheet(driver)
    if notif_BottomSheet.is_permission_button_displayed():
        notif_BottomSheet.click_Permission_button()
        print("Clicked on permission button")

    #     # # اعتبارسنجی نتیجه لاگین (فرضاً صفحه اصلی نمایش داده می‌شود)
    home_page = HomePage(driver)
    assert home_page.get_welcome_message() == "خانه"
    print("Verified welcome message")

    # اعتبارسنجی اینکه دکمه "Not Now" کار می‌کند و به صفحه صحیح منتقل می‌شود
    # شما باید اینجا ادامه صفحه بعد از بومتریک را اعتبارسنجی کنید، برای مثال:
    # assert some_page.is_displayed(), "Some page should be displayed after clicking 'Not Now' button"
    print("Test completed successfully")

    # پس از اتمام تست، بستن درایور
    driver.quit()
