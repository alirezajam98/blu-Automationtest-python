import random
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


def national_code_generator():
    number_list = []
    total_sum = 0

    for i in range(10, 1, -1):
        j = random.randint(0, 9)
        number_list.append(str(j))
        total_sum += j * i

    m = total_sum % 11
    if m < 2:
        number_list.append(str(m))
    else:
        number_list.append(str(11 - m))

    national_code = ''.join(number_list)
    return national_code
import random
import time

def national_code_generator_Round():
    # تنظیم seed برای تصادفی تر کردن خروجی‌ها
    random.seed(time.time())

    number_list = []
    total_sum = 0

    # تولید نهایتاً 4 عدد تصادفی منحصر به فرد
    similar_numbers = [random.randint(0, 9) for _ in range(3)]

    # حلقه برای تولید اعداد تصادفی از مجموعه مشابه و محاسبه جمع کل
    for i in range(10, 1, -1):
        j = random.choice(similar_numbers)  # انتخاب یک عدد از مجموعه مشابه
        number_list.append(str(j))  # افزودن عدد به لیست
        total_sum += j * i  # محاسبه جمع کل با ضرایب مشخص

    # محاسبه مقدار m
    m = total_sum % 11
    if m < 2:
        number_list.append(str(m))
    else:
        number_list.append(str(11 - m))

    # ترکیب اعداد در لیست به یک رشته
    national_code = ''.join(number_list)
    return national_code
