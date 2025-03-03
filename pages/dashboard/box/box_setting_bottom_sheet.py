from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.dashboard.box.select_box_name_page import CreateBoxPage
from pages.dashboard.box.box_confirm_modal import BoxConfirmModal


class BoxSettingBottomSheet(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title_text(self):
        """دریافت متن عنوان"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        return self.get_element_text(locator)

    def get_description_text(self):
        """دریافت متن توضیحات"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")
        return self.get_element_text(locator)

    def click_edit_name(self):
        """کلیک روی دکمه ویرایش نام و هدایت به صفحه تغییر نام باکس"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(2)')
        self.click_element(locator)

    def click_delete_box(self):
        """کلیک روی دکمه حذف باکس و باز کردن مودال تأیید حذف"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("برداشت موجودی و حذف")')
        self.click_element(locator)

    def click_cancel_delete(self):
        """کلیک روی دکمه لغو در مودال حذف"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/cancelButton")
        self.click_element(locator)

    def click_confirm_delete(self):
        """کلیک روی دکمه تأیید حذف"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton")
        self.click_element(locator)