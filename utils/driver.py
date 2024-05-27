import yaml
from appium import webdriver


def create_driver():
    # خواندن پیکربندی‌ها از فایل config.yml
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)

    desired_caps = config['desired_caps']
    server_url = config['server_url']
    implicit_wait = config['implicit_wait']

    driver = webdriver.Remote(server_url, desired_caps)
    driver.implicitly_wait(implicit_wait)
    return driver


if __name__ == "__main__":
    create_driver()
