from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.dashboard.box.box_page import BoxPage  # وارد کردن کلاس صفحه اصلی باکس
from pages.dashboard.box.box_profile_page import BoxProfilePage  # وارد کردن کلاس صفحه پروفایل باکس


class BoxConfirmModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_modal_displayed(self):
        """بررسی نمایش مودال تأیید حذف"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        return self.is_element_visible(locator)

    def get_title_text(self):
        """دریافت عنوان مودال"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        return self.get_element_text(locator)

    def get_subtitle_text(self):
        """دریافت زیرعنوان مودال"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/subtitleTextView")
        return self.get_element_text(locator)

    def get_description_text(self):
        """دریافت توضیحات مودال"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")
        return self.get_element_text(locator)

    def cancel_delete(self):
        """کلیک روی دکمه کنسل و بازگشت به صفحه پروفایل باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/cancelButton")
        self.click_element(locator)

    def confirm_delete(self):
        """کلیک روی دکمه تأیید حذف و هدایت به صفحه اصلی باکس"""
        locator = (AppiumBy.ID, 'com.samanpr.blu.dev:id/deleteButton')
        self.click_element(locator)
