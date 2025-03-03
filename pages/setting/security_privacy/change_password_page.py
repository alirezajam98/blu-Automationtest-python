from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ChangePasswordPage(BasePage):
    def get_page_title(self):
        """دریافت عنوان صفحه تغییر رمز عبور"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر رمز عبور']"))

    def enter_old_password(self, password):
        """وارد کردن رمز عبور فعلی"""
        self.input_text((AppiumBy.ID, "com.samanpr.blu.dev:id/oldPasswordEditText"), password)

    def enter_new_password(self, password):
        """وارد کردن رمز عبور جدید"""
        self.input_text((AppiumBy.ID, "com.samanpr.blu.dev:id/newPasswordEditText"), password)

    def click_confirm_button(self):
        """کلیک روی دکمه تأیید و ذخیره"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/acceptButton"))

    def get_error_message(self):
        """دریافت پیام خطا (در صورت وجود)"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/snakbarMessageTextView"))

    def is_confirm_button_enabled(self):
        """بررسی فعال بودن دکمه تأیید و ذخیره"""
        return self.is_element_enabled((AppiumBy.ID, "com.samanpr.blu.dev:id/acceptButton"))
