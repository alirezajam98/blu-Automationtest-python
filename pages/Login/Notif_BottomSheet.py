from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class Notif_BottomSheet(BasePage):
    Permission_BTN_Allow = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')

    def click_Permission_button(self):
        self.click(self.Permission_BTN_Allow)
