import time

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ChangePhonePage(BasePage):
    def get_page_title(self):
        """دریافت عنوان صفحه تغییر شماره تلفن همراه"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر شماره تلفن همراه']"))

    def get_input_hint(self):
        """دریافت متن راهنما (Hint) فیلد ورودی شماره تلفن"""
        return self.get_element_attribute(
            (AppiumBy.ID, "com.samanpr.blu.dev:id/phoneInputEditText"), "hint"
        )

    def get_guide_text(self):
        """دریافت متن راهنما (در ادامه کد تایید برای شما ارسال می‌شود)"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/guideTextView"))

    def enter_phone_number(self, phone_number):
        """وارد کردن شماره تلفن جدید"""
        self.input_text(
            (AppiumBy.ID, "com.samanpr.blu.dev:id/phoneInputEditText"), phone_number
        )

    def click_next_button(self):
        """کلیک روی دکمه ادامه"""
        time.sleep(3)
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))

    def is_next_button_enabled(self):
        """بررسی فعال بودن دکمه ادامه"""
        return self.is_element_enabled((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))