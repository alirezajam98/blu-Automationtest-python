import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class TransferPage(BasePage):
    def close_onboarding(self, timeout=60):
        time.sleep(2)
        """بستن صفحه انبوردینگ"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/actionButton")
        self.click_element(locator, timeout)

    def get_transfer_page_title_text(self):
        """دریافت متن عنوان صفحه انتقال"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/toolbarTitleTextView")
        return self.get_element_text(locator)

    def get_promo_title_text(self):
        """دریافت متن عنوان تبلیغ انتقال به مخاطبین"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        return self.get_element_text(locator)

    def get_promo_description_text(self):
        """دریافت متن توضیحات تبلیغ"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.samanpr.blu.dev:id/contentTextView")')
        return self.get_element_text(locator)

    def click_activate_button(self):
        """کلیک روی دکمه 'فعال کردن'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/actionButton")
        self.click_element(locator)

    def click_cancel_button(self):
        """کلیک روی دکمه 'الان نه'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/cancelButton")
        self.click_element(locator)

    def get_destinations_header_text(self):
        """دریافت متن هدر 'مقصدها'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/headerTitleTextView")
        return self.get_element_text(locator)

    def get_empty_state_title_text(self):
        """دریافت متن عنوان حالت خالی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("مقصد انتقالی ندارید")')
        return self.get_element_text(locator)

    def get_empty_state_description_text(self):
        """دریافت متن توضیحات حالت خالی"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")
        return self.get_element_text(locator)

    def click_new_transfer_button(self):
        """کلیک روی دکمه 'انتقال جدید'"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/fabNewTransfer")
        self.click_element(locator)

    def scroll(self):

        window_size = self.driver.get_window_size()  # ?????? ?????? ????
        start_x = window_size['width'] * 0.5  # 50% ??? ????
        start_y = window_size['height'] * 0.2
        end_y = window_size['height'] * 0.9

        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)  # ???? ?? ?????? ????
        actions.w3c_actions.pointer_action.pointer_down()  # ???? ? ?????????
        actions.w3c_actions.pointer_action.move_to_location(start_x, end_y)  # ???? ?? ?????? ?????
        actions.w3c_actions.pointer_action.release()  # ??? ???? ????
        actions.perform()