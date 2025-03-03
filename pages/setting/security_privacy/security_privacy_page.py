from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class SecurityPrivacyPage(BasePage):
    def get_page_title(self):
        """دریافت عنوان صفحه امنیت و حریم خصوصی"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='امنیت و حریم خصوصی']"))

    def get_change_password_text(self):
        """دریافت متن گزینه تغییر رمز عبور"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر رمز عبور']"))

    def get_transaction_password_text(self):
        """دریافت متن گزینه رمز تراکنش"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='رمز تراکنش']"))

    def get_my_devices_text(self):
        """دریافت متن گزینه دستگاه‌های من"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='دستگاه‌های من']"))

    def get_transfer_to_contacts_text(self):
        """دریافت متن گزینه انتقال وجه به مخاطبین"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='انتقال وجه به مخاطبین']"))

    def get_logout_text(self):
        """دریافت متن گزینه خروج از حساب کاربری"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='خروج از حساب کاربری']"))

    def click_change_password(self):
        """کلیک روی گزینه تغییر رمز عبور"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر رمز عبور']"))

    def click_transaction_password(self):
        """کلیک روی گزینه رمز تراکنش"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='رمز تراکنش']"))

    def click_my_devices(self):
        """کلیک روی گزینه دستگاه‌های من"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='دستگاه‌های من']"))

    def click_transfer_to_contacts(self):
        """کلیک روی گزینه انتقال وجه به مخاطبین"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='انتقال وجه به مخاطبین']"))

    def click_logout(self):
        """کلیک روی گزینه خروج از حساب کاربری"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='خروج از حساب کاربری']"))

    def confirm_logout(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/actionButton"))

    def cancel_logout(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/cancelButton"))