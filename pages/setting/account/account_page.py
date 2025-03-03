from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class AccountPage(BasePage):
    def get_account_page_title(self):
        """دریافت عنوان صفحه حساب کاربری"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='حساب کاربری']"))

    def bank_account_option(self):
        """دریافت متن گزینه حساب بانکی"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='حساب بانکی']"))

    def click_bank_account_option(self):
        """کلیک روی گزینه حساب بانکی"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='حساب بانکی']"))

    def change_phone_option(self):
        """دریافت متن گزینه تغییر شماره تلفن همراه"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر شماره تلفن همراه']"))

    def click_change_phone_option(self):
        """کلیک روی گزینه تغییر شماره تلفن همراه"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر شماره تلفن همراه']"))

    def change_address_option(self):
        """دریافت متن گزینه تغییر آدرس محل سکونت"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر آدرس محل سکونت']"))

    def click_change_address_option(self):
        """کلیک روی گزینه تغییر آدرس محل سکونت"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر آدرس محل سکونت']"))

    def change_job_option(self):
        """دریافت متن گزینه تغییر شغل"""
        return self.get_element_text((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر شغل']"))

    def click_change_job_option(self):
        """کلیک روی گزینه تغییر شغل"""
        self.click_element((AppiumBy.XPATH, "//android.widget.TextView[@text='تغییر شغل']"))

    def toast_text(self):
        """دریافت متن Toast"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/snakbarMessageTextView"))

class BankAccountBottomSheet(BasePage):
    def title(self):
        """دریافت عنوان باتم‌شیت"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView"))

    def description(self):
        """دریافت توضیحات باتم‌شیت"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView"))

    def account_holder(self):
        """دریافت نام دارنده حساب"""
        return self.get_element_text((AppiumBy.XPATH, '//android.widget.TextView[@text="‏دارنده حساب"]'))

    def join_date(self):
        """دریافت تاریخ پیوستن به بلو"""
        return self.get_element_text((AppiumBy.XPATH, '//android.widget.TextView[@text="‏تاریخ پیوستن به بلو"]'))

    def account_type(self):
        """دریافت نوع حساب"""
        return self.get_element_text((AppiumBy.XPATH, '//android.widget.TextView[@text="‏نوع حساب"]'))

    def account_number(self):
        """دریافت شماره حساب"""
        return self.get_element_text((AppiumBy.XPATH, 'new UiSelector().text("‏شماره حساب")'))

    def iban_number(self):
        """دریافت شماره شبا"""
        return self.get_element_text((AppiumBy.XPATH, '//android.widget.TextView[@text="‏شماره شبا"]'))

    def click_close_account(self):
        """کلیک روی دکمه بستن حساب"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/terminateButton"))

    def close_account_button(self):
        """دریافت متن دکمه بستن حساب"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/terminateButton"))

    def other_saman_accounts_button(self):
        """دریافت متن دکمه سایر حساب های بانک سامان"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/samanAccountsButton"))

    def click_other_saman_accounts(self):
        """کلیک روی دکمه سایر حساب های بانک سامان"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/samanAccountsButton"))

    def get_account_holder_name(self):
        """دریافت نام دارنده حساب"""
        return self.get_element_text((AppiumBy.XPATH, '//android.widget.TextView[@text="‏امیر کنارنگ"]'))

    def get_join_date_value(self):
        """دریافت مقدار تاریخ پیوستن به بلو"""
        return self.get_element_text((AppiumBy.XPATH, '//android.widget.TextView[@text="‏۳۰ آبان ۱۴۰۳"]'))

    def get_account_type_value(self):
        """دریافت مقدار نوع حساب"""
        return self.get_element_text((AppiumBy.XPATH, '//android.widget.TextView[@text="‏سپرده کوتاه مدت"]'))

    def get_account_number_value(self):
        """دریافت مقدار شماره حساب"""
        return self.get_element_text((AppiumBy.XPATH, '//android.widget.TextView[@text="‏۶۱۱۸۲۸۰۰۳۰۰۰۳۷۳۵۰۱"]'))

    def get_iban_number_value(self):
        """دریافت مقدار شماره شبا"""
        return self.get_element_text(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="‏IR - ۹۴ ۰۵۶۰ ۶۱۱۸ ۲۸۰۰ ۳۰۰۰ ۳۷۳۵ ۰۱"]'))


class CloseAccountConfirmationDialog(BasePage):
    def get_dialog_title(self):
        """دریافت عنوان دیالوگ"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView"))

    def get_dialog_description(self):
        """دریافت توضیحات دیالوگ"""
        return self.get_element_text((AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView"))

    def click_cancel_button(self):
        """کلیک روی دکمه انصراف"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/tertiaryCancelButton"))

    def click_confirm_close_button(self):
        """کلیک روی دکمه تأیید بستن حساب"""
        self.click_element((AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton"))

