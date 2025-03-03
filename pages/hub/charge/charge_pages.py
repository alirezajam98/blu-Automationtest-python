from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ChargePages(BasePage):
    def click_charge_option(self):
        """کلیک روی گزینه 'شارژ'"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شارژ")')
        self.click_element(locator)

    def get_page_title_text(self):
        """دریافت متن عنوان صفحه"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/pageTitleTextView")
        return self.get_element_text(locator)

    def click_title_text_view(self):
        """کلیک روی عنوان صفحه"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        self.click_element(locator)

    def get_description_text(self):
        """دریافت متن توضیحات"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")
        return self.get_element_text(locator)

    def click_fab_new(self):
        """کلیک روی دکمه 'جدید'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/fabNew")
        self.click_element(locator)

    def enter_phone_number(self, phone_number):
        """وارد کردن شماره تلفن"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/phoneEditText")
        self.send_keys(locator, phone_number)

    def click_confirm_button(self):
        """کلیک روی دکمه 'تایید'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton")
        self.click_element(locator)

    def get_error_message(self):
        """دریافت پیام خطا"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/textinput_error")
        return self.get_element_text(locator)

    def select_operator(self, operator_name):
        """انتخاب اپراتور (همراه اول، ایرانسل، رایتل، شاتل موبایل، سامانتل)"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{operator_name}")')
        self.click_element(locator)

    def click_payment_button(self):
        """کلیک روی دکمه 'پرداخت'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/paymentButton")
        self.click_element(locator)

    def select_charge_amount(self, amount):
        """انتخاب مبلغ شارژ"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{amount}")')
        self.click_element(locator)

    def get_top_title_text(self):
        """دریافت متن عنوان بالای صفحه"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/topTitleTextView")
        return self.get_element_text(locator)

    def click_accept_button(self):
        """کلیک روی دکمه 'قبول'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/acceptButton")
        self.click_element(locator)

    def get_transfer_status(self):
        """دریافت وضعیت انتقال"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/transferStatusChip")
        return self.get_element_text(locator)

    def click_go_to_top(self):
        """کلیک روی دکمه 'رفتن به بالا'"""
        locator = (AppiumBy.ACCESSIBILITY_ID, "رفتن به بالا")
        self.click_element(locator)