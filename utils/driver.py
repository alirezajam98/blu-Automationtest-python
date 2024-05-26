from appium import webdriver


def create_driver():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'S23 Ultra',
        'udid': 'R5CW517VZ9F',
        'platformVersion': '14',
        'automationName': 'UiAutomator2',
        'appPackage': 'com.samanpr.blu.dev',
        'appActivity': 'com.samanpr.blu.presentation.BaseActivity',
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    return driver


create_driver()
