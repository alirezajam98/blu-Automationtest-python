from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def clear(self, locator):
        self.find_element(locator).clear()

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()
