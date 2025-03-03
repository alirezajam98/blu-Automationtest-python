from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CardSecuritySettingsPages(BasePage):
    def change_first_password_button(self):
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/changeFirstPasswordButton'))

    def change_first_password_button_title(self):
        return self.get_element_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/changeFirstPasswordButton'))

    def forgot_first_password_button(self):
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/forgotFirstPasswordButton'))

    def forgot_first_password_button_title(self):
        return self.get_element_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/forgotFirstPasswordButton'))

    def change_first_password_page_title(self):
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("تغییر رمز اول")'))

    def forgot_first_password_page_title(self):
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("فراموشی رمز اول")'))

    def set_password_page_subtitle(self):
        return self.get_element_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/titleTextView'))

    def set_password_field_text(self):
        return self.get_element_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/passwordInputEditText'))

    def input_password(self, password):
        self.input_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/passwordInputEditText'), password)

    def clear_input_password(self):
        self.clear_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/passwordInputEditText'))

    def set_password_confirm_field_text(self):
        return self.get_element_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/confirmPasswordInputEditText'))

    def input_confirm_password(self, password):
        self.input_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/confirmPasswordInputEditText'), password)

    def clear_input_confirm_password(self):
        self.clear_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/confirmPasswordInputEditText'))

    def confirm_button(self):
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/activateButton'))

    def password_input_error(self):
        return self.get_element_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/textinput_error'))

    def password_not_match_error(self):
        return self.get_element_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/textinput_error'))

    def password_len_error(self):
        return self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("رمز ۴ رقمی لازم است")'))

    def password_confirm_len_error(self):
        return self.get_element_text(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("تکرار رمز ۴ رقمی لازم است")'))
