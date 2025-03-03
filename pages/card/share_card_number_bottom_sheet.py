from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ShareCardNumberBottomSheet(BasePage):
    def card_number_title(self):
        """دریافت عنوان شماره کارت"""
        return self.get_element_text(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شماره کارت")')
        )

    def card_number(self):
        """دریافت شماره کارت"""
        return self.get_element_text(
            (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='com.samanpr.blu.dev:id/cardNumberRowView']/android.widget.TextView[2]")
        )

    def sheba_number_title(self):
        """دریافت عنوان شماره شبا"""
        return self.get_element_text(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شماره شبا")')
        )

    def sheba_number(self):
        """دریافت شماره شبا"""
        return self.get_element_text(
            (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='com.samanpr.blu.dev:id/shebaNumberRowView']/android.widget.TextView[2]")
        )

    def copy_card_number_button(self):
        """کلیک روی دکمه کپی شماره کارت"""
        self.click_element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
        )

    def copy_sheba_number_button(self):
        """کلیک روی دکمه کپی شماره شبا"""
        self.click_element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)')
        )

    def toast_text(self):
        """دریافت متن Toast"""
        return self.get_element_text(
            (AppiumBy.ID, "com.samanpr.blu.dev:id/snakbarMessageTextView")
        )
