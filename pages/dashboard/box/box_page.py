from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class BoxPage(BasePage):
    def close_onboarding(self, timeout=40):
        """بستن صفحه انبوردینگ"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/actionButton")
        self.click_element(locator, timeout)

    def is_box_page_displayed(self):
        """بررسی نمایش صفحه باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/boxesDepositTextView")
        return self.is_element_visible(locator)

    def get_box_deposit_text(self):
        """دریافت متن موجودی باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/boxesDepositTextView")
        return self.get_element_text(locator)

    def get_box_deposit_description(self):
        """دریافت توضیحات موجودی باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/boxesDepositDescriptionTextView")
        return self.get_element_text(locator)

    def get_no_active_box_title(self):
        """دریافت عنوان 'باکس فعالی ندارید'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        return self.get_element_text(locator)

    def get_no_active_box_description(self):
        """دریافت توضیحات 'باکس فعالی ندارید'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")
        return self.get_element_text(locator)

    def click_new_box(self):
        """کلیک روی دکمه ایجاد باکس جدید"""
        locator = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.samanpr.blu.dev:id/fabNewSpace']")
        self.click_element(locator)

    def get_first_box_name(self):
        """دریافت نام اولین باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        return self.get_element_text(locator)

    def get_first_box_amount(self):
        """دریافت مقدار اولین باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")
        return self.get_element_text(locator)

    def click_first_box(self):
        """کلیک روی اولین باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/spaceView")
        self.click_element(locator)
