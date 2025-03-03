import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class CardPage(BasePage):
    def page_title(self):
        """دریافت عنوان صفحه"""
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR,
                                      'new UiSelector().resourceId("com.samanpr.blu.dev:id/toolbarTitleTextView")'))

    def scroll_menu(self):
        """اسکرول کردن سال با استفاده از ActionChains با مختصات نسبی"""
        window_size = self.driver.get_window_size()  # دریافت اندازه صفحه
        start_x = window_size['width'] * 0.5  # 50% عرض صفحه
        start_y = window_size['height'] * 0.5  # 80% ارتفاع صفحه (مختصات شروع)
        end_y = window_size['height'] * 0.9  # 20% ارتفاع صفحه (مختصات پایان)

        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)  # حرکت به مختصات شروع
        actions.w3c_actions.pointer_action.pointer_down()  # کلیک و نگه‌داشتن
        actions.w3c_actions.pointer_action.move_to_location(start_x, end_y)  # حرکت به مختصات پایان
        actions.w3c_actions.pointer_action.release()  # رها کردن کلیک
        actions.perform()

    def blu_card(self):
        """کلیک روی بلو کارت"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/rotateButton"), timeout=20)

    def blu_card_freeze(self):
        """بررسی وجود و نمایش دکمه مسدودسازی بلو کارت"""
        assert self.is_element_visible((AppiumBy.ID, "com.samanpr.blu.dev:id/realisticCardOverlayImageView")), \
            "Error: 'Blu Card Freeze' button is not visible."

    def card_number_text(self):
        """دریافت شماره کارت بلو کارت"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/textViewCardNumber"))

    def share_card_number_button(self):
        """کلیک روی دکمه اشتراک شماره کارت"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/shareButton"))

    def share_card_number_button_title(self):
        """دریافت عنوان دکمه اشتراک شماره کارت"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/shareButton"))

    def pin2_button(self):
        """کلیک روی دکمه رمز دوم پویا"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/pin2Button"))

    def check_enable_pin2_button(self):
        """بررسی غیرفعال بودن دکمه رمز دوم پویا"""
        assert not self.is_element_enabled((AppiumBy.ID, "com.samanpr.blu.dev:id/pin2Button")), \
            "Error: 'Pin2' button is enabled, but it should be disabled."

    def pin2_button_title(self):
        """دریافت عنوان دکمه رمز دوم پویا"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/pin2Button"))

    def freeze_button_title(self):
        """دریافت عنوان دکمه مسدودسازی موقت"""
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("مسدودسازی موقت")'))

    def is_switch_on(self):
        """بررسی وضعیت روشن یا خاموش بودن سوئیچ"""
        return self.get_element_attribute((AppiumBy.CLASS_NAME, 'android.widget.Switch'), "checked") == "true"

    def freeze_toggle_switch(self):
        """تغییر وضعیت سوئیچ مسدودسازی"""
        self.click_element((AppiumBy.CLASS_NAME, 'android.widget.Switch'))

    def freeze_button_subtitle(self):
        """دریافت متن زیرعنوان دکمه مسدودسازی موقت"""
        return self.get_element_text(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("بلوکارت را بصورت موقت غیرفعال کنید")'))

    def card_security_setting_button_title(self):
        """دریافت عنوان دکمه تنظیمات امنیتی"""
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("تنظیمات امنیتی")'))

    def card_security_setting_button_subtitle(self):
        """دریافت متن زیرعنوان دکمه تنظیمات امنیتی"""
        return self.get_element_text(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("تغییر و دریافت مجدد رمز بلوکارت")'))

    def card_security_setting_button(self):
        """کلیک روی دکمه تنظیمات امنیتی"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().resourceId("com.samanpr.blu.dev:id/cardSecuritySettings").instance(0)'))

    def check_enable_card_security_setting_button(self):
        """بررسی غیرفعال بودن دکمه تنظیمات امنیتی"""
        assert not self.is_element_enabled((AppiumBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().resourceId("com.samanpr.blu.dev:id/cardSecuritySettings'
                                            '").instance(0)')), \
            "Error: 'Card Security Setting' button is enabled, but it should be disabled."

    def change_blu_card_button_title(self):
        """دریافت عنوان دکمه تعویض بلو کارت"""
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("تعویض بلوکارت")'))

    def change_blu_card_button_subtitle(self):
        """دریافت متن زیرعنوان دکمه تعویض بلو کارت"""
        return self.get_element_text(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("می‌توانید بلوکارت جدید سفارش دهید")'))

    def change_blu_card_button(self):
        """کلیک روی دکمه تعویض بلو کارت"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().text("تعویض بلوکارت")'))

    def deactivate_button_title(self):
        """دریافت عنوان دکمه غیر فعال کردن"""
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("غیر فعال کردن")'))

    def deactivate_button_subtitle(self):
        """دریافت متن زیرعنوان دکمه غیر فعال کردن"""
        return self.get_element_text(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("مسدودسازی بلوکارت در صورت مفقودی و …")'))

    def deactivate_button(self):
        """کلیک روی دکمه غیر فعال کردن"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiSelector().resourceId('com.samanpr.blu.dev:id/cardSecuritySettings').instance(2)"))

    def toast_text(self):
        """دریافت متن Toast"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/snakbarMessageTextView"))
