import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class HubPage(BasePage):
    def scroll(self):

        """اسکرول کردن سال با استفاده از ActionChains با مختصات نسبی"""
        window_size = self.driver.get_window_size()  # دریافت اندازه صفحه
        start_x = window_size['width'] * 0.5  # 50% عرض صفحه
        start_y = window_size['height'] * 0.2
        end_y = window_size['height'] * 0.9

        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)  # حرکت به مختصات شروع
        actions.w3c_actions.pointer_action.pointer_down()  # کلیک و نگه‌داشتن
        actions.w3c_actions.pointer_action.move_to_location(start_x, end_y)  # حرکت به مختصات پایان
        actions.w3c_actions.pointer_action.release()  # رها کردن کلیک
        actions.perform()

    def click_qr_title(self):
        """کلیک روی عنوان QR"""
        self.click_element((AppiumBy.ID, 'com.samanpr.blu.dev:id/qrTitleTextView'))

    def get_qr_title_text(self):
        """دریافت متن عنوان QR"""
        locator = (AppiumBy.ID, 'com.samanpr.blu.dev:id/qrTitleTextView')
        return self.get_element_text(locator)

    def click_charge(self):
        """کلیک روی گزینه شارژ"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شارژ")'))

    def get_charge_text(self):
        """دریافت متن گزینه شارژ"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("شارژ")')
        return self.get_element_text(locator)

    def click_internet(self):
        """کلیک روی گزینه اینترنت"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("اینترنت")'))

    def get_internet_text(self):
        """دریافت متن گزینه اینترنت"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("اینترنت")')
        return self.get_element_text(locator)

    def click_bill(self):
        """کلیک روی گزینه قبض"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("قبض")'))

    def get_bill_text(self):
        """دریافت متن گزینه قبض"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("قبض")')
        return self.get_element_text(locator)

    def click_refund(self):
        """کلیک روی گزینه برگشت پول"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("برگشت پول")'))

    def get_refund_text(self):
        """دریافت متن گزینه برگشت پول"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("برگشت پول")')
        return self.get_element_text(locator)

    def click_loan(self):
        """کلیک روی گزینه وام"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("وام")'))

    def get_loan_text(self):
        """دریافت متن گزینه وام"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("وام")')
        return self.get_element_text(locator)

    def click_auto_payment(self):
        """کلیک روی گزینه پرداخت خودکار"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("پرداخت خودکار")'))

    def get_auto_payment_text(self):
        """دریافت متن گزینه پرداخت خودکار"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("پرداخت خودکار")')
        return self.get_element_text(locator)

    def click_dong(self):
        """کلیک روی گزینه دُنگ"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                          '"com.samanpr.blu.dev:id/iconImageView").instance(6)'))

    def get_dong_text(self):
        """دریافت متن گزینه دُنگ"""
        locator = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.samanpr.blu.dev:id/titleTextView" and '
                                  '@text="دُنگ‌"]')
        return self.get_element_text(locator)

    def click_check(self):
        """کلیک روی گزینه چک صیادی"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("چک صیادی")'))

    def get_check_text(self):
        """دریافت متن گزینه چک صیادی"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("چک صیادی")')
        return self.get_element_text(locator)

    def click_car_services(self):
        """کلیک روی گزینه خدمات خودرو"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("خدمات خودرو")'))

    def get_car_services_text(self):
        """دریافت متن گزینه خدمات خودرو"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("خدمات خودرو")')
        return self.get_element_text(locator)

    def click_invite_friends(self):
        """کلیک روی گزینه دعوت دوستان"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("دعوت دوستان")'))

    def get_invite_friends_text(self):
        """دریافت متن گزینه دعوت دوستان"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("دعوت دوستان")')
        return self.get_element_text(locator)

    def click_junior(self):
        """کلیک روی گزینه جونیور"""
        self.click_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("جونیور")'))

    def get_junior_text(self):
        """دریافت متن گزینه جونیور"""
        locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("جونیور")')
        return self.get_element_text(locator)
