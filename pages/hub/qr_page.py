import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class QrPage(BasePage):
    def click_back(self):
        """کلیک روی دکمه بازگشت"""
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "رفتن به بالا"))

    def toggle_flash(self):
        """تغییر حالت فلش"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/actionFlash"))

    def open_support(self):
        """باز کردن پنل پشتیبانی"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/actionSupport"))

    def open_my_qr(self):
        """باز کردن QR کد کاربر"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/scanButton"))

    def open_my_qr_title(self):
        """باز کردن QR کد کاربر"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/scanButton"))

    def open_gallery(self):
        """باز کردن گالری برای انتخاب تصویر"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/galleryButton"))

    def is_scan_area_visible(self):
        """بررسی وجود ناحیه اسکن"""
        return self.is_element_visible((AppiumBy.ID, "com.samanpr.blu.dev:id/scanAnimationView"))

    def get_page_title(self):
        """دریافت عنوان صفحه"""
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("اسکن کد QR")'))


class MyQrPage(BasePage):
    def get_title_my_qr_page(self):
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("برای دریافت پول، کد QR خود '
                                                                    'را نمایش دهید")'))

    def get_add_price_title(self):
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("افزودن مبلغ")'))

    def get_share_title(self):
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ارسال / ذخیره")'))

    def click_amount(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/amountButton"))

    def get_toast_text(self):
        return self.get_element_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/snakbarMessageTextView'))


class AddPricePage(BasePage):

    def get_page_title(self):
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("مبلغ کد QR")'))

    def get_add_price_title(self):
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView"))

    def get_amount_field_text(self):
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/amountEditText"))

    def input_amount(self, price):
        self.input_text((AppiumBy.ID, "com.samanpr.blu.dev:id/amountEditText"), price)

    def get_save_button_title(self):
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/saveButton"))

    def click_save_button_title(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/saveButton"))

    def get_remove_button_title(self):
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/removeButton"))

    def click_remove_button_title(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/removeButton"))