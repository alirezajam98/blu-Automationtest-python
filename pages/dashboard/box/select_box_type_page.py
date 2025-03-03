# pages/select_box_type_page.py
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.dashboard.box.box_profile_page import BoxProfilePage
from pages.dashboard.box.select_box_name_page import CreateBoxPage


class SelectBoxTypePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_normal_box(self):
        """انتخاب باکس عادی"""
        locator = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='com.samanpr.blu.dev:id/wealthBoxType'])[1]")
        self.click_element(locator)
        return CreateBoxPage(self.driver)

    def select_long_term_box(self):
        """انتخاب باکس بلندمدت"""
        locator = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='com.samanpr.blu.dev:id/wealthBoxType'])[2]")
        self.click_element(locator)
        return BoxProfilePage(self.driver)

    def is_page_displayed(self):
        """بررسی نمایش صفحه انتخاب نوع باکس"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView["
                                   "@resource-id='com.samanpr.blu.dev:id/descriptionTextView' and @text='نوع باکس خود"
                                   " را انتخاب کنید']")
        return self.is_element_visible(locator)

    def get_normal_box_title(self):
        """دریافت عنوان باکس عادی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("بلوباکس")')
        return self.get_element_text(locator)

    def get_normal_box_description(self):
        """دریافت توضیحات باکس عادی"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView["
                                   "@resource-id='com.samanpr.blu.dev:id/descriptionTextView' and @text='فضایی برای "
                                   "پس‌انداز هدفمند یا مدیریت مخارج با سود کوتاه‌مدت']")
        return self.get_element_text(locator)

    def get_long_term_box_title(self):
        """دریافت عنوان باکس بلندمدت"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.samanpr.blu.dev:id/titleTextView' and "
                                   "@text='بیگ‌باکس']")
        return self.get_element_text(locator)

    def get_long_term_box_description(self):
        """دریافت توضیحات باکس بلندمدت"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView["
                                   "@resource-id='com.samanpr.blu.dev:id/descriptionTextView' and @text='فضایی برای "
                                   "سپرده‌گذاری بلندمدت تا ۲۲ درصد سود به صورت سالیانه']")
        return self.get_element_text(locator)

    def is_normal_box_title_correct(self):
        """بررسی صحت عنوان باکس عادی"""
        return self.get_normal_box_title() == "بلوباکس"

    def is_normal_box_description_correct(self):
        """بررسی صحت توضیحات باکس عادی"""
        return self.get_normal_box_description() == "فضایی برای پس‌انداز هدفمند یا مدیریت مخارج با سود کوتاه‌مدت"

    def is_long_term_box_title_correct(self):
        """بررسی صحت عنوان باکس بلندمدت"""
        return self.get_long_term_box_title() == "بیگ‌باکس"

    def is_long_term_box_description_correct(self):
        """بررسی صحت توضیحات باکس بلندمدت"""
        return self.get_long_term_box_description() == "فضایی برای سپرده‌گذاری بلندمدت تا ۲۲ درصد سود به صورت سالیانه"
