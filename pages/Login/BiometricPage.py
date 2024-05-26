from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class Biometric(BasePage):
    BTN_NOT_NOW = (AppiumBy.ID, 'com.samanpr.blu.dev:id/btnNotNow')
    CLOSE_BUTTON = (AppiumBy.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                    '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android'
                    '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
                    '/android.widget.ImageButton')
    FINGER_IMG = (AppiumBy.ID, 'com.samanpr.blu.dev:id/ivFaceId')
    DESCRIPTION = (AppiumBy.ID, 'com.samanpr.blu.dev:id/descriptionTextView')
    BTN_ENABLE = (AppiumBy.ID, 'com.samanpr.blu.dev:id/btnEnable')

    def get_description(self):
        return self.get_attribute(self.DESCRIPTION, "text")

    def get_btn_enable_text(self):
        return self.get_attribute(self.BTN_ENABLE, "text")

    def is_btn_enable_displayed(self):
        return self.is_displayed(self.BTN_ENABLE)

    def get_btn_not_now_text(self):
        return self.get_attribute(self.BTN_NOT_NOW, "text")

    def is_btn_not_now_displayed(self):
        return self.is_displayed(self.BTN_NOT_NOW)

    def click_btn_not_now(self):
        self.click(self.BTN_NOT_NOW)
        # Assuming GeneralClass is another page object
        # return GeneralClass(self.driver)
        # If GeneralClass is not defined, we can return self for chaining
        return self

    def click_not_now_change_password(self):
        self.click(self.BTN_NOT_NOW)
        # Assuming SettingPage is another page object
        # return SettingPage(self.driver)
        # If SettingPage is not defined, we can return self for chaining
        return self

    def click_not_now_kyc(self):
        self.click(self.BTN_NOT_NOW)
        # Assuming CreateAccountPage is another page object
        # return CreateAccountPage(self.driver)
        # If CreateAccountPage is not defined, we can return self for chaining
        return self
