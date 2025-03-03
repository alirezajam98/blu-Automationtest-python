import time

from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from utils.common_flows import logger


class ChangeBluCardPage(BasePage):
    def same_pan_button(self):
        """کلیک روی دکمه 'شماره کارت فعلی'"""
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/samePanButton'))

    def same_pan_text(self):
        """دریافت متن المان شماره کارت فعلی"""
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR,
                                      'new UiSelector().resourceId("com.samanpr.blu.dev:id/titleTextView").text("شماره کارت فعلی")'))

    def back_button(self):
        """کلیک روی دکمه 'بازگشت به بالا'"""
        time.sleep(5)
        self.click_element((AppiumBy.ACCESSIBILITY_ID, "رفتن به بالا"))

    def card_number(self):
        """دریافت متن شماره کارت از المان"""
        try:
            elements = self.driver.find_elements(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("com.samanpr.blu.dev:id/subtitleTextView")'
            )
            if len(elements) > 1:
                return elements[1].get_attribute("text")  # متن دومین المان
            else:
                logger.error("Element with index 1 not found.")
                return None
        except Exception as e:
            logger.error(f"Error in card_number method: {str(e)}")
            return None

    def same_pan_modal_title(self):
        self.get_element_text((AppiumBy.ID,"com.samanpr.blu.dev:id/titleTextView"))

    def same_pan_modal_subtitle(self):
        self.get_element_text((AppiumBy.ID,"com.samanpr.blu.dev:id/subtitleTextView"))

    def same_pan_modal_confirm_button_text(self):
        self.get_element_text((AppiumBy.ID,"com.samanpr.blu.dev:id/confirmButton"))

    def same_pan_modal_cancel_button_text(self):
        self.get_element_text((AppiumBy.ID,"com.samanpr.blu.dev:id/cancelButton"))

    def same_pan_modal_confirm_button(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))

    def same_pan_modal_cancel_button(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/cancelButton"))

