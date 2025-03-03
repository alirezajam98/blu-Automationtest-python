import time

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class PermissionsDialog(BasePage):
    def allow_notification_permission(self):
        """اجازه دسترسی به نوتیفیکیشن (اگر مجوز درخواست شد)"""
        self.click_element((AppiumBy.ID, "com.android.permissioncontroller:id"
                                                        "/permission_allow_button"))

    def allow_camera_permission(self):
        """اجازه دسترسی به دوربین (اگر مجوز درخواست شد)"""
        self.click_element((AppiumBy.ID, "com.android.permissioncontroller:id"
                                                        "/permission_allow_foreground_only_button"))
