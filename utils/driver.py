import yaml
from appium import webdriver

def create_driver(device_name):
    # خواندن تنظیمات از فایل desired_caps.yml
    with open('config.yml', 'r') as file:
        desired_caps_config = yaml.safe_load(file)

    # یافتن تنظیمات مربوط به دستگاه مورد نظر بر اساس نام دستگاه
    desired_caps = desired_caps_config['desired_caps'][device_name]

    # استخراج سایر تنظیمات
    server_url = desired_caps_config['server_url']
    implicit_wait = desired_caps_config['implicit_wait']

    # ایجاد درایور با تنظیمات مشخص شده
    driver = webdriver.Remote(server_url, desired_caps)
    driver.implicitly_wait(implicit_wait)
    return driver

if __name__ == "__main__":
    # فراخوانی تابع create_driver با ارسال نام دستگاه مورد نظر
    create_driver('A23s')
    create_driver('A10s')

