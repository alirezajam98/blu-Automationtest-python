from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class TransactionPinPage(BasePage):
    # سایر متدهای موجود...

    def enable_transaction_password(self):
        """فعال‌سازی رمز تراکنش با کلیک روی سوئیچ"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Switch")'))

    def enter_transaction_password(self):
        """وارد کردن رمز تراکنش"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/numberOneTextview"))

    def confirm_transaction_password(self, password):
        """تأیید رمز تراکنش"""
        self.enter_transaction_password(password)

    def is_transaction_password_enabled(self):
        """بررسی فعال بودن رمز تراکنش"""
        return self.get_element_attribute((AppiumBy.XPATH, "//android.widget.Switch[@resource-id='com.samanpr.blu.dev:id/enableRowView']"), "checked") == "true"

    def click_change_transaction_password(self):
        """کلیک روی گزینه تغییر رمز تراکنش"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/changeRowView"))
    def click_forget_transaction_password(self):
        """کلیک روی گزینه فراموشی رمز تراکنش"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='فراموشی رمز تراکنش']"))