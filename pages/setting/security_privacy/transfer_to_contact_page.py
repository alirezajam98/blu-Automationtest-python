from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class TransferToContactPage(BasePage):
    # سایر متدهای موجود...

    def enable_transfer_to_contacts(self):
        """فعال‌سازی انتقال وجه به مخاطبین با کلیک روی سوئیچ"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/activationSwitchRowView"))

    def accept_terms_and_conditions(self):
        """فعال‌سازی انتقال وجه به مخاطبین با کلیک روی سوئیچ"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Switch")'))

    def is_transfer_to_contacts_enabled(self):
        """بررسی فعال بودن انتقال وجه به مخاطبین"""
        return self.get_element_attribute(
            (AppiumBy.XPATH, "//android.widget.Switch[@resource-id='com.samanpr.blu.dev:id/activationSwitchRowView']"),
            "checked") == "true"

    def confirm_disable(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/actionButton"))

    def click_confirm_button(self):
        """کلیک روی دکمه تأیید در صفحه فعال‌سازی"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))

    def click_confirm_button_sysytem_allow_permission(self):
        """کلیک روی دکمه تأیید در صفحه فعال‌سازی"""
        self.click_element((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button"))
