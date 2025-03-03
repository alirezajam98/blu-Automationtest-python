from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import os
from utils.utils import logger, save_account_to_file


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    # متدهای مربوط به ورود، جستجو و تأیید مشتری
    def login_sub_title(self):
        login_sub_title_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/span"))
        )
        return login_sub_title_element.text

    def enter_username(self, username):
        username_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div/div[2]/div/div/span/input"))
        )
        username_element.click()
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/div/div[2]/div/div/span/input"))
        )
        password_element.click()
        password_element.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[3]/button/div"))
        )
        login_button.click()

    def blu_main_queue(self):
        main_queue = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/div/main/div/div[2]/div[1]/div/div[3]/div/div"))
        )
        main_queue.click()

    def search(self):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/main/div/div[4]/button/div"))
        )
        search_box.click()
    def enter_customer_username(self, username):
        customer_username_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/main/div/div[6]/form/div[1]/div[1]/div/div/div/div/div/span/input"))
        )
        customer_username_field.click()
        customer_username_field.send_keys(username)
        print("نام کاربری وارد شد")
    def list_siah_check(self):
        check_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div/div/main/div/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/label/span[1]"))
        )
        check_box.click()

    def confirm_customer_button(self):
        confirm_customer = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div/div/main/div/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]"))
        )
        confirm_customer.click()

    def final_confirm_customer_button(self):
        final_confirm_customer = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div/div[3]/button[2]"))
        )
        final_confirm_customer.click()

    def select_first_customer(self):
        first_customer = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/main/div/div[7]/div/div/div/div/div/div/table/tbody/tr[2]/td[4]"))
        )
        first_customer.click()
        print("مشتری اول انتخاب شد")

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/main/div/div[6]/form/div[2]/div[1]/button/div"))
        )
        search_button.click()
        print("گزینه جستجو انتخاب شد")
    def search_username_until_found(self, max_attempts=5):
        for attempt in range(max_attempts):
            username = f"blu_auto{attempt}"  # تولید نام کاربری فرضی
            print(f"تلاش {attempt + 1}: جستجوی نام کاربری {username}")
            customer_username_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/html/body/div/div/div/div/main/div/div[6]/form/div[1]/div[1]/div/div/div/div/div/span/input"))
            )
            customer_username_field.clear()  # پاک کردن فیلد جستجو
            customer_username_field.send_keys(username)
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div/div/div/div/main/div/div[6]/form/div[2]/div[1]/button/div"))
            )
            search_button.click()
            sleep(2)
            try:
                first_customer = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                "/html/body/div/div/div/div/main/div/div[7]/div/div/div/div/div/div/table/tbody/tr[2]/td[4]"))
                )
                first_customer.click()
                print(f"مشتری با نام کاربری {username} پیدا شد.")
                return
            except:
                print(f"نام کاربری {username} پیدا نشد. تلاش بعدی.")

        print("تعداد تلاش‌های مجاز به پایان رسید. مشتری پیدا نشد.")


def run_main_process(username):
    # تنظیمات درایور
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from time import sleep

    chromedriver_path = "C:\\Users\\a.jamshidi\\Documents\\chromedriver.exe"
    service = ChromeService(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://kyc-panel-uat.sdb247.com/")
    driver.maximize_window()
    sleep(1)

    mainpage = MainPage(driver)

    # ورود به سیستم
    mainpage.enter_username("s.mofarah")
    mainpage.enter_password("Ss@123456")
    mainpage.click_login_button()
    mainpage.blu_main_queue()

    # جستجو و تأیید مشتری
    print("شروع جستجوی مشتری و تأیید")
    mainpage.search()
    sleep(1)

    mainpage.enter_customer_username(username)

    mainpage.click_search_button()

    try:
        # انتخاب اولین مشتری
        mainpage.select_first_customer()
        mainpage.list_siah_check()
        mainpage.confirm_customer_button()
        mainpage.final_confirm_customer_button()
        save_account_to_file(username)
        logger.info(f"مشتری با نام کاربری {username} با موفقیت تأیید شد.")
    except Exception as e:
        logger.error(f"خطا در تأیید مشتری: {e}")
        driver.quit()
        raise

    driver.quit()
