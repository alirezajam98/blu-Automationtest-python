from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class Notif_BottomSheet:
    def __init__(self, driver):
        self.driver = driver

    def is_permission_button_displayed(self):
        try:
            return self.driver.find_element_by_id("permission_button_id").is_displayed()
        except NoSuchElementException:
            return False

    def click_Permission_button(self):
        self.driver.find_element_by_id("permission_button_id").click()
