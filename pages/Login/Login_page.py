# from pages.base_page import BasePage
# from appium.webdriver.common.appiumby import AppiumBy
#
# class LoginPage(BasePage):
#     FIRST_EDIT_TEXT = (AppiumBy.ID, 'com.samanpr.blu.dev:id/firstEditText')
#     SECOND_EDIT_TEXT = (AppiumBy.ID, 'com.samanpr.blu.dev:id/secondEditText')
#     LOGIN_BUTTON = (AppiumBy.ID, 'com.samanpr.blu.dev:id/confirm')
#
#     def enter_first_text(self, text):
#         self.enter_text(self.FIRST_EDIT_TEXT, text)
#
#     def enter_second_text(self, text):
#         self.enter_text(self.SECOND_EDIT_TEXT, text)
#
#     def click_login_button(self):
#         self.click(self.LOGIN_BUTTON)


from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from pages.Login.BiometricPage import Biometric


class LoginPage(BasePage):
    SUPPORT_BUTTON = (AppiumBy.ID, "com.samanpr.blu:id/actionButton")
    IMAGE_VIEW_LOGO_TYPE = (AppiumBy.ID, "com.samanpr.blu.dev:id/imageViewLogoType")
    USERNAME_FIELD = (AppiumBy.ID, "com.samanpr.blu.dev:id/firstEditText")
    PASSWORD_FIELD = (AppiumBy.ID, "com.samanpr.blu.dev:id/secondEditText")
    CONFIRM_BUTTON = (AppiumBy.ID, "com.samanpr.blu.dev:id/confirm")
    RECOVERY_BUTTON = (AppiumBy.ID, "com.samanpr.blu.dev:id/recoveryButton")
    ERR_TXT1 = (AppiumBy.ID, "com.samanpr.blu.dev:id/hintTV")
    ERR_TXT2 = (AppiumBy.XPATH, "/hierarchy/android.widget.Toast")
    UAT = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                           ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                           ".FrameLayout/android.view.ViewGroup[2]/android.widget.TextView[1]")
    STAGE = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                             ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.view.ViewGroup[4]/android.widget.TextView[1]")
    OPEN_ACCOUNT = (AppiumBy.ID, "com.samanpr.blu.dev:id/openButton")

    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)
        return self

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)
        return self

    def clear_username_field(self):
        self.clear(self.USERNAME_FIELD)
        return self

    def clear_password_field(self):
        self.clear(self.PASSWORD_FIELD)
        return self

    def press_login_button(self):
        self.click(self.CONFIRM_BUTTON)
        return Biometric(self.driver)

    def click_open_account(self):
        self.click(self.OPEN_ACCOUNT)
        # Assuming StartPage is another page object
        # return StartPage(self.driver)
        # If StartPage is not defined, we can return self for chaining
        return self

    def is_biometric_page_displayed(self):
        return self.is_displayed(self.CONFIRM_BUTTON)

    def get_error_text(self):
        return self.get_attribute(self.ERR_TXT1, "text")

    def get_open_account_text(self):
        return self.get_attribute(self.OPEN_ACCOUNT, "text")

    def get_username_text(self):
        return self.get_attribute(self.USERNAME_FIELD, "text")

    def get_error_text_1(self):
        return self.get_attribute(self.ERR_TXT2, "text")

    def get_password_text(self):
        return self.get_attribute(self.PASSWORD_FIELD, "text")

    def get_confirm_button_text(self):
        return self.get_attribute(self.CONFIRM_BUTTON, "text")

    def get_recovery_button_text(self):
        return self.get_attribute(self.RECOVERY_BUTTON, "text")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        return self.press_login_button()

    def click_on_logo(self):
        self.click(self.IMAGE_VIEW_LOGO_TYPE)
        return self

    def click_uat(self):
        self.click(self.UAT)
        return self

    def click_uat_start_page(self):
        self.click(self.UAT)
        # Assuming CreateAccountOnBoardingPage is another page object
        # return CreateAccountOnBoardingPage(self.driver)
        # If CreateAccountOnBoardingPage is not defined, we can return self for chaining
        return self

    def click_stage(self):
        self.click(self.STAGE)
        return self
