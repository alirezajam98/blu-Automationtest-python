# from time import sleep
#
# import pytest
#
# from pages.HomePage import HomePage
# from pages.Login.Login_page import LoginPage
# from utils.driver import create_driver
# from pages.Login.BiometricPage import Biometric
# from pages.Login.Notif_BottomSheet import Notif_BottomSheet
# @pytest.fixture(scope='function')
# def driver():
#     driver = create_driver()
#     yield driver
#     driver.quit()
#
# def test_login_with_biometric(driver):
#     login_page = LoginPage(driver)
#
#     # وارد کردن یوزرنیم و پسورد
#     login_page.enter_first_text('aljm')
#     login_page.enter_second_text('Bb123456')
#
#     # کلیک بر روی دکمه لاگین
#     login_page.click_login_button()
#
#
#     # ورود به صفحه بومتریک
#     biometric_page = Biometric(driver)
#     biometric_page.click_btn_not_now()
#
#     # کلیک بر روی allow برای دسترسی به نوتیفیکیشن
#     notif_BottomSheet = Notif_BottomSheet(driver)
#     notif_BottomSheet.click_Permission_button()
#
#
#     # # اعتبارسنجی نتیجه لاگین (فرضاً صفحه اصلی نمایش داده می‌شود)
#     home_page = HomePage(driver)
#     assert home_page.get_welcome_message() == "خانه"

import pytest

from pages.HomePage import HomePage
from pages.Login.Login_page import LoginPage
from pages.Login.Notif_BottomSheet import Notif_BottomSheet
from utils.driver import create_driver


# @pytest.fixture(scope='function')
@pytest.mark.login
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


def test_login_with_biometric(driver):
    login_page = LoginPage(driver)

    # وارد کردن یوزرنیم و پسورد
    login_page.enter_username('aljm')
    login_page.enter_password('Bb123456')

    # کلیک بر روی دکمه لاگین
    biometric_page = login_page.press_login_button()

    # اعتبارسنجی ورود به صفحه بومتریک
    assert biometric_page.is_btn_not_now_displayed(), "Biometric page should be displayed after login"

    # کلیک بر روی دکمه "Not Now" در صفحه بومتریک
    biometric_page.click_btn_not_now()
    # کلیک بر روی allow برای دسترسی به نوتیفیکیشن
    notif_BottomSheet = Notif_BottomSheet(driver)
    notif_BottomSheet.click_Permission_button()

    #     # # اعتبارسنجی نتیجه لاگین (فرضاً صفحه اصلی نمایش داده می‌شود)
    home_page = HomePage(driver)
    assert home_page.get_welcome_message() == "خانه"

    # اعتبارسنجی اینکه دکمه "Not Now" کار می‌کند و به صفحه صحیح منتقل می‌شود
    # شما باید اینجا ادامه صفحه بعد از بومتریک را اعتبارسنجی کنید، برای مثال:
    # assert some_page.is_displayed(), "Some page should be displayed after clicking 'Not Now' button"
