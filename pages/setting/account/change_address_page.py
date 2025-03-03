import time

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ChangeAddressPage(BasePage):
    def get_page_title(self):
        """دریافت عنوان صفحه تغییر آدرس محل سکونت"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر آدرس محل سکونت']"))

    def get_input_hint(self):
        """دریافت متن راهنما (Hint) فیلد ورودی کدپستی"""
        return self.get_element_attribute(
            (AppiumBy.ID, "com.samanpr.blu.dev:id/postalCodeInputEditText"), "hint"
        )

    def enter_postal_code(self, postal_code):
        """وارد کردن کدپستی"""
        self.input_text(
            (AppiumBy.ID, "com.samanpr.blu.dev:id/postalCodeInputEditText"), postal_code
        )

    def click_continue_button(self):
        """کلیک روی دکمه ادامه"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/showAddressButton"))
        time.sleep(15)

    def is_continue_button_enabled(self):
        """بررسی فعال بودن دکمه ادامه"""
        return self.is_element_enabled((AppiumBy.ID, "com.samanpr.blu.dev:id/showAddressButton"))

    def click_continue_button_in_map(self):
        """کلیک روی دکمه ادامه"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))


class EditAddressPage(BasePage):
    def get_page_title(self):
        """دریافت عنوان صفحه ویرایش آدرس"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر آدرس محل سکونت']"))

    def get_province_city_value(self):
        """دریافت مقدار استان و شهر (فقط نمایشی)"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/provinceCityInputEditText"))

    def get_street_value(self):
        """دریافت مقدار خیابان اصلی (فقط نمایشی)"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/streetInputEditText"))

    def get_avenue_value(self):
        """دریافت مقدار خیابان فرعی (فقط نمایشی)"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/avenueInputEditText"))

    def enter_unit(self, unit):
        """وارد کردن بلوک، طبقه، واحد (تنها فیلد قابل ویرایش)"""
        self.input_text(
            (AppiumBy.ID, "com.samanpr.blu.dev:id/unitInputEditText"), unit
        )

    def click_confirm_button(self):
        """کلیک روی دکمه تأیید و ذخیره"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))
        time.sleep(3)
    def is_confirm_button_enabled(self):
        """بررسی فعال بودن دکمه تأیید و ذخیره"""
        return self.is_element_enabled((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))