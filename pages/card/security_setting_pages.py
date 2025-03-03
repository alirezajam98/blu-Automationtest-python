from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SecuritySettingPages(BasePage):
    def card_number_title(self):
        """دریافت عنوان شماره کارت"""
        return self.get_element_text(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شماره کارت")')
        )
