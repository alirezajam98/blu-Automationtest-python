import time

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SettingPage(BasePage):
    def click_account(self):
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("حساب کاربری")'))

    def get_user_account_text(self):
        """دریافت متن گزینه حساب کاربری"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("حساب کاربری")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def click_security_privacy(self):
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("امنیت و حریم خصوصی")'))

    def get_security_and_privacy_text(self):
        """دریافت متن گزینه امنیت و حریم خصوصی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("امنیت و حریم خصوصی")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_notifications_text(self):
        """دریافت متن گزینه اطلاع‌رسانی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("اطلاع‌رسانی")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_notifications_subtext(self):
        """دریافت متن فرعی گزینه اطلاع‌رسانی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("تنظیمات نوتیفیکیشن")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_blu_club_text(self):
        """دریافت متن گزینه بلوکلاب"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("بلوکلاب")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_blu_club_subtext(self):
        """دریافت متن فرعی بلوکلاب"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("فعالیت بیشتر، جایزه بیشتر")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_support_text(self):
        """دریافت متن گزینه پشتیبانی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("پشتیبانی")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_support_subtext(self):
        """دریافت متن فرعی گزینه پشتیبانی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("گفتگو، تماس و سوالات متداول")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_update_text(self):
        """دریافت متن گزینه به‌روزرسانی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("به‌روزرسانی")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_update_subtext(self):
        """دریافت متن فرعی گزینه به‌روزرسانی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("بررسی نسخه برنامه")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_display_blu_text(self):
        """دریافت متن گزینه نمایش بلو"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("نمایش بلو")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_display_blu_subtext(self):
        """دریافت متن فرعی گزینه نمایش بلو"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("حالت روز و شب، آیکون برنامه")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_invite_friends_text(self):
        """دریافت متن گزینه دعوت دوستان"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("دعوت دوستان")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_invite_friends_subtext(self):
        """دریافت متن فرعی گزینه دعوت دوستان"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("بلوکارت مشکی و هدیه نقدی برای شما")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_feedback_text(self):
        """دریافت متن گزینه ثبت ایده‌ها و نظرات"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ثبت ایده‌ها و نظرات")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_feedback_subtext(self):
        """دریافت متن فرعی گزینه ثبت ایده‌ها و نظرات"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("رشد و بهبود بلو با همراهی شما")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_blu_text(self):
        """دریافت متن فرعی گزینه بلو"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("بلو")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_blu_subtext(self):
        """دریافت متن فرعی گزینه بلو"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("قوانین و شرایط، درباره ما")')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_version_text(self):
        """دریافت متن نسخه برنامه"""
        locator = (AppiumBy.ID, 'com.samanpr.blu.dev:id/versionTextView')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)

    def get_made_in_text(self):
        """دریافت متن Made In"""
        locator = (AppiumBy.ID, 'com.samanpr.blu.dev:id/madeInTextView')
        self.scroll_to_element(locator)
        return self.get_element_text(locator)
