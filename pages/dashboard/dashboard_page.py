import time

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def get_balance_text(self):
        """دریافت متن موجودی حساب"""
        locator = (AppiumBy.ID, 'com.samanpr.blu.dev:id/balanceTextView')
        return self.get_element_text(locator)

    def click_charge_button(self):
        """کلیک روی دکمه شارژ حساب"""
        locator = (AppiumBy.ID, 'com.samanpr.blu.dev:id/chargeButton')
        self.click_element(locator)

    def get_charge_button_text(self):
        """دریافت متن دکمه شارژ حساب"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شارژ حساب")')
        return self.get_element_text(locator)

    def click_box_button(self):
        """کلیک روی دکمه باکس"""
        locator = (AppiumBy.ID, 'com.samanpr.blu.dev:id/boxButton')
        self.click_element(locator)
        time.sleep(2)

    def get_box_button_text(self):
        """دریافت متن دکمه باکس"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("باکس")')
        return self.get_element_text(locator)

    def click_analytics_button(self):
        """کلیک روی دکمه گزارش مالی"""
        locator = (AppiumBy.ID, 'com.samanpr.blu.dev:id/analyticsButton')
        self.click_element(locator)

    def get_analytics_button_text(self):
        """دریافت متن دکمه گزارش مالی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("گزارش مالی")')
        return self.get_element_text(locator)

    def get_no_transaction_text(self):
        """دریافت متن 'تراکنشی ندارید'"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("تراکنشی ندارید")')
        return self.get_element_text(locator)

    def get_no_transaction_description(self):
        """دریافت متن توضیحات 'اولین تراکنش خود را انجام دهید'"""
        locator = (AppiumBy.ID, 'com.samanpr.blu.dev:id/descriptionTextView')
        return self.get_element_text(locator)

    def dashboard_tab_button(self):
        """کلیک روی گزینه صورتحساب در منوی پایین"""
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/nav_invoice'))

    def transfer_tab_button(self):
        """کلیک روی گزینه انتقال در منوی پایین"""
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/nav_transfer'))

    def hub_tab_button(self):
        """کلیک روی گزینه فروشگاه در منوی پایین"""
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/nav_payment'))

    def card_tab_button(self):
        """کلیک روی گزینه کارت در منوی پایین"""
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/nav_card'))

    def click_settings_button(self):
        """کلیک روی گزینه تنظیمات در منوی پایین"""
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/nav_settings'))
