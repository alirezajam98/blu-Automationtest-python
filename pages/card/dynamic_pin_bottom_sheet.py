from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class DynamicPinBottomSheet(BasePage):
    def pin2_bottom_sheet_title(self):
        """دریافت متن عنوان باتم‌شیت رمز دوم پویا"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView"))

    def card_number(self):
        """دریافت شماره کارت از باتم‌شیت رمز دوم پویا"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView"))

    def dynamic_pin(self):
        """دریافت متن رمز دوم پویا"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/dynamicPinTextView"))

    def copy_dynamic_button_pin_title(self):
        """دریافت عنوان دکمه کپی رمز دوم پویا"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/copyButton"))

    def copy_dynamic_button_pin(self):
        """کلیک روی دکمه کپی رمز دوم پویا"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/copyButton"))

    def toast_text(self):
        """دریافت متن Toast برای تایید کپی رمز دوم پویا"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/snakbarMessageTextView"))
