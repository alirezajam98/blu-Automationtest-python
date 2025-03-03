import time

from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from utils.common_flows import logger


class CardFirstOrderPages(BasePage):

    def name_of_user(self):
        self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView"))

    def confirm_open_account_message(self):
        self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView"""))

    def start_card_order_button_title(self):
        self.get_element_text((AppiumBy, "com.samanpr.blu.dev:id/openButton"))

    def start_card_order_button(self):
        """کلیک روی دکمه سفارش کارت"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/openButton"))

    def card_order_page_title(self):
        self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("سفارش بلوکارت")'))

    def select_blu_card_color_title(self):
        self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView"))

    def card_color(self):
        self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/cardNameTextView"))

    def select_right_color(self):
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className('
                                                          '"android.view.ViewGroup").instance(7)'))

    def accept_button_text(self):
        self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/acceptButton"))

    def accept_button(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/acceptButton"))

    def address_modal_title(self):
        self.get_element_text((AppiumBy.ID, 'com.samanpr.blu.dev:id/titleTextView'))

    def address_modal_subtitle(self):
        self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView"))

    def address_modal_confirm_button_text(self):
        self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))

    def address_modal_confirm_button(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))

    def postal_code_page_title(self):
        self.get_element_text((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("آدرس محل سکونت")'))

    def postal_code_title(self):
        self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView"))

    def postal_code_field_text(self):
        self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/postalCodeInputEditText"))

    def postal_code_field(self, text):
        """وارد کردن کد پستی در فیلد مربوطه"""
        self.input_text((AppiumBy.ID, "com.samanpr.blu.dev:id/postalCodeInputEditText"), text)

    def confirm_postal_code_button(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/showAddressButton"))

    def confirm_postal_code_button_text(self):
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/showAddressButton"))
