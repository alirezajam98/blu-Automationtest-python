from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from utils.config import logger


class BasePage:
    DEFAULT_TIMEOUT = 5

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT

        """عمومی برای یافتن المان"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT

        """کلیک روی یک المان"""
        element = self.find_element(locator, timeout)
        element.click()

    def get_element_text(self, locator, attribute="text", timeout=None):
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)

    def input_text(self, locator, text, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT

        """وارد کردن متن در یک فیلد"""
        element = self.find_element(locator, timeout)
        element.send_keys(text)

    def clear_text(self, locator, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT

        """پاک کردن متن فیلد"""
        element = self.find_element(locator, timeout)
        element.clear()

    def is_element_enabled(self, locator, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT

        """بررسی فعال یا غیرفعال بودن یک المان"""
        element = self.find_element(locator, timeout)
        return element.is_enabled()

    def is_element_visible(self, locator, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT

        """بررسی قابل مشاهده بودن المان"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_element_attribute(self, locator, attribute, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT

        """دریافت مقدار یک اتریبیوت از المان"""
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)

    def scroll_to_element(self, locator):
        """اسکرول به یک المان خاص"""
        try:
            logger.info(f"در حال جستجوی عنصر با متن")
            self.driver.find_element(*locator)
        except Exception as e:
            logger.warning(f"اسکرول برای پیدا کردن عنصر با متن")
            if locator[0] == AppiumBy.ANDROID_UIAUTOMATOR or locator[0] == '-android uiautomator':
                self.driver.find_element(
                    '-android uiautomator',
                    f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView({locator[1]})'
                )
            else:
                raise Exception(f"استراتژی اسکرول پشتیبانی نمی‌شود برای locator: {locator} - خطا: {e}")
