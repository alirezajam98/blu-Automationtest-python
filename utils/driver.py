import yaml
from appium import webdriver


def create_driver(desired_caps):
    with open('config.yml', 'r') as file:
        desired_caps_config = yaml.safe_load(file)

    server_url = desired_caps_config['server_url']
    driver = webdriver.Remote(server_url, desired_caps)
    driver.implicitly_wait(desired_caps_config['implicit_wait'])
    return driver
