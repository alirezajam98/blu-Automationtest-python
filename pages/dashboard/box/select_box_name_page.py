from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.dashboard.box.box_profile_page import BoxProfilePage
from utils.config import logger


class CreateBoxPage(BasePage):
    """صفحه ایجاد باکس جدید برای تعریف نام و ذخیره باکس."""

    PRESET_NAMES = {
        "پس‌انداز ماهانه": "پس‌انداز ماهانه",
        "خرید ماشین": "خرید ماشین",
        "سفر": "سفر"
    }

    def __init__(self, driver):
        super().__init__(driver)

    def enter_box_name(self, box_name, timeout=10):
        """وارد کردن نام باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/spaceNameEditText")
        self.input_text(locator, box_name, timeout)

    def save_new_box(self, timeout=10):
        """کلیک روی دکمه ساخت باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton")
        if self.is_element_visible(locator, timeout):
            self.click_element(locator)
            return BoxProfilePage(self.driver)
        else:
            raise Exception("دکمه ساخت باکس یافت نشد.")

    def is_page_displayed(self, timeout=10):
        """بررسی نمایش صفحه ایجاد باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/spaceNameEditText")
        return self.is_element_visible(locator, timeout)

    def get_page_title(self, timeout=10):
        """دریافت عنوان صفحه"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='باکس جدید']")
        return self.get_element_text(locator, timeout)

    def click_back_button(self, timeout=10):
        """کلیک روی دکمه بازگشت"""
        locator = (AppiumBy.ACCESSIBILITY_ID, "رفتن به بالا")
        self.click_element(locator, timeout)

    def click_change_image(self, timeout=10):
        """کلیک روی دکمه تغییر عکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/changeImageTextView")
        self.click_element(locator, timeout)

    def get_box_name_character_count(self, timeout=10):
        """دریافت تعداد کاراکترهای نام باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/spaceLengthTextView")
        return self.get_element_text(locator, timeout)

    def select_preset_name(self, preset_name, timeout=10):
        """انتخاب نام از پیش تعیین شده"""
        if preset_name not in self.PRESET_NAMES:
            raise ValueError(f"نام از پیش تعیین شده '{preset_name}' معتبر نیست.")
        locator = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{self.PRESET_NAMES[preset_name]}']")
        self.click_element(locator, timeout)

    def is_create_box_button_enabled(self, timeout=10):
        """بررسی فعال بودن دکمه ساخت باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton")
        return self.is_element_enabled(locator, timeout)

    def get_box_image(self, timeout=10):
        """دریافت تصویر باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/avatarImageView")
        return self.is_element_visible(locator, timeout)

    def close_keyboard(self):
        """بستن کیبورد"""
        try:
            self.driver.hide_keyboard()
            logger.info("کیبورد بسته شد.")
        except Exception as e:
            logger.warning(f"کیبورد بسته نشد یا باز نبود: {str(e)}")