from .base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class HomePage(BasePage):
    WELCOME_MESSAGE = (AppiumBy.ID, 'com.samanpr.blu.dev:id/titleTextView')

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MESSAGE)
