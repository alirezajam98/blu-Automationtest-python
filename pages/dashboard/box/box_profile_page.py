from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class BoxProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_active_goal_status(self):
        """دریافت وضعیت فعال هدف"""
        locator = (AppiumBy.XPATH, "//android.view.ViewGroup[contains(@resource-id, 'status_goal_active')]")
        return self.get_element_text(locator)

    def click_box_settings(self):
        """کلیک روی دکمه تنظیمات باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/settingsButton")
        self.click_element(locator)

    def click_back_to_box_page(self):
        """بازگشت به صفحه باکس"""
        locator = (AppiumBy.ACCESSIBILITY_ID, "رفتن به بالا")
        self.click_element(locator)

    def get_box_profile_title(self):
        """دریافت عنوان پروفایل باکس"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView[contains(@resource-id, 'box_profile_name')]")
        return self.get_element_text(locator)

    def check_image_box_profile(self):
        """بررسی نمایش تصویر پروفایل باکس"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/avatarImageView")
        return self.is_element_visible(locator)

    def get_save_amount(self):
        """دریافت مبلغ ذخیره شده"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/priceTextView")
        return self.get_element_text(locator)

    def get_desc_amount(self):
        """دریافت توضیحات مبلغ"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView[contains(@resource-id, 'desc_amount')]")
        return self.get_element_text(locator)

    def get_deposit_btn_text(self):
        """دریافت متن دکمه واریز"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/depositButton")
        return self.get_element_text(locator)

    def click_deposit_btn(self):
        """کلیک روی دکمه واریز"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/depositButton")
        self.click_element(locator)

    def get_withdraw_btn_text(self):
        """دریافت متن دکمه برداشت"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/withdrawButton")
        return self.get_element_text(locator)

    def click_withdraw_btn(self):
        """کلیک روی دکمه برداشت"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/withdrawButton")
        self.click_element(locator)

    def check_setting_button(self):
        """بررسی وجود دکمه تنظیمات"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/settingsButton")
        return self.is_element_visible(locator)

    def get_goal_title(self):
        """دریافت عنوان هدف"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView[contains(@resource-id, 'title_goal')]")
        return self.get_element_text(locator)

    def get_activation_goal_desc(self):
        """دریافت توضیحات فعال‌سازی هدف"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView[contains(@resource-id, 'activation_goal_desc')]")
        return self.get_element_text(locator)

    def get_status_goal(self):
        """دریافت وضعیت هدف"""
        locator = (AppiumBy.XPATH, "//android.view.ViewGroup[contains(@resource-id, 'status_goal')]")
        return self.get_element_text(locator)

    def check_add_goal_button(self):
        """بررسی وجود دکمه افزودن هدف"""
        locator = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@resource-id, 'add_goal_button')]")
        return self.is_element_visible(locator)

    def get_round_up_title(self):
        """دریافت عنوان Round Up"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView[contains(@resource-id, 'title_round_up')]")
        return self.get_element_text(locator)

    def get_activation_round_up_desc(self):
        """دریافت توضیحات فعال‌سازی Round Up"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView[contains(@resource-id, 'activation_round_up_desc')]")
        return self.get_element_text(locator)

    def get_status_round_up(self):
        """دریافت وضعیت Round Up"""
        locator = (AppiumBy.XPATH, "//android.view.ViewGroup[contains(@resource-id, 'status_round_up')]")
        return self.get_element_text(locator)

    def get_title_transaction_box_profile(self):
        """دریافت عنوان تراکنش‌ها"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/transactionTitleTextView")
        return self.get_element_text(locator)

    def check_empty_state_image(self):
        """بررسی تصویر حالت خالی"""
        locator = (AppiumBy.ID, "com.samanpr.blu.dev:id/illustrationView")
        return self.is_element_visible(locator)

    def get_empty_state_desc(self):
        """دریافت توضیحات حالت خالی"""
        locator = (AppiumBy.XPATH, "//android.widget.TextView[contains(@resource-id, 'empty_state_desc')]")
        return self.get_element_text(locator)