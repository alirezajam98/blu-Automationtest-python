import json

from utils.utils import logger, load_accounts
import allure
import pytest
from appium.webdriver.appium_service import AppiumService
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.common.base import AppiumOptions
from devices.device_config import device_configs
from pages.dashboard.dashboard_page import DashboardPage
from utils.utils import load_confirmed_accounts


# فیکسچر برای مدیریت اتصال به WebDriver
@pytest.fixture(scope="function")  # اجرا برای هر تست
def setup(request):
    """
    راه‌اندازی WebDriver برای اتصال به دستگاه
    و بستن آن پس از اتمام تست.
    """
    # دریافت نام دستگاه از آرگومان‌های pytest
    device_name = request.config.getoption("--device_name")
    # پیکربندی قابلیت‌های Appium برای دستگاه
    options = AppiumOptions()
    options.load_capabilities(device_configs[device_name])

    try:
        # اتصال به WebDriver با استفاده از Appium
        logger.info(f"Connecting to WebDriver on http://127.0.0.1:4723 for device '{device_name}'")
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    except Exception as e:
        logger.error(f"Failed to connect to WebDriver: {e}")
        raise

    yield driver  # بازگرداندن درایور برای استفاده در تست

    # بستن اتصال WebDriver
    logger.info("Closing WebDriver connection.")
    driver.quit()


# افزودن گزینه‌های سفارشی به pytest برای دریافت device_name و device_udid
def pytest_addoption(parser):
    """
    اضافه کردن آرگومان‌های سفارشی به pytest:
    - --device_name: نام دستگاه برای اجرای تست‌ها (پیش‌فرض: 'Galaxy A11').
    - --device_udid: شناسه دستگاه برای اتصال (پیش‌فرض: رشته خالی).
    """
    parser.addoption("--device_name", action="store", default="Galaxy A11", help="Device name for the tests")
    parser.addoption("--device_udid", action="store", default="", help="Device UDID")


# فیکسچر برای دریافت device_name از آرگومان‌های pytest
@pytest.fixture
def device_name(request):
    """
    فیکسچر برای دریافت مقدار --device_name از آرگومان‌های pytest.
    این مقدار توسط تست‌ها استفاده می‌شود.
    """
    return request.config.getoption("--device_name")


# فیکسچر برای دریافت مقدار `--device_udid` از آرگومان‌های pytest
@pytest.fixture
def device_udid(request):
    """
    فیکسچر برای گرفتن مقدار آرگومان --device_udid که توسط pytest اضافه شده است.
    این مقدار شناسه دستگاه (UDID) را برای تست‌ها فراهم می‌کند.
    """
    return request.config.getoption("--device_udid")


# فیکسچر برای باز کردن اپلیکیشن بدون نیاز به ورود به سیستم
@pytest.fixture
def open_app_without_login(setup):
    """
    این فیکسچر اپلیکیشن را بدون ورود به حساب کاربری باز می‌کند.
    از فیکسچر `setup` برای راه‌اندازی WebDriver استفاده می‌کند.
    """
    driver = setup  # دریافت WebDriver از فیکسچر `setup`
    logger.info("App opened without logging in.")  # ثبت لاگ برای باز شدن اپلیکیشن
    yield driver  # بازگرداندن درایور برای استفاده در تست‌ها


# فیکسچر برای لاگین و هدایت به صفحه داشبورد، وابسته به setup
@pytest.fixture
def login_and_dashboard(request):
    from pages.login_page import LoginPage
    device_name = request.config.getoption("--device_name")
    options = AppiumOptions()
    options.load_capabilities(device_configs[device_name])

    service = AppiumService()
    service.start()
    #
    # # دریافت username از پارامتر درخواست (در صورت وجود)
    # username = request.param if hasattr(request, "param") else "andpfm7"

    if isinstance(request.param, dict):
        username = request.param.get("username")
        password_key = request.param.get("password_key", "pass1")
    else:
        username = request.param  # برای سازگاری با تست‌های موجود
        password_key = "pass1"

        # بارگیری اطلاعات حساب‌ها
    accounts = load_accounts()

    # بررسی وجود نام کاربری در فایل
    if username not in accounts:
        raise ValueError(f"Username '{username}' not found in accounts.json!")

    # دریافت پسورد
    password = accounts[username].get(password_key)
    if not password:
        raise ValueError(f"Password key '{password_key}' not found for user '{username}'!")

    appium_url = "http://127.0.0.1:4723"
    driver = webdriver.Remote(appium_url, options=options)

    try:
        allow_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(allow_button)
        )
        driver.find_element(*allow_button).click()
        logger.info("Clicked on 'Allow' button for notification permission.")
    except TimeoutException:
        logger.info("No notification permission modal displayed, continuing.")

    with allure.step("Click on 'has Account' button"):
        try:
            logger.info("کلیک روی دکمه 'حساب کاربری دارم'...")
            has_account_button = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/hasAccountButton"))
            )
            has_account_button.click()
            logger.info("دکمه 'حساب کاربری دارم' کلیک شد.")
        except TimeoutException:
            logger.info("No Create Account button displayed, continuing.")

    # بررسی دسترسی نوتیفیکیشن (Allow)
    try:
        allow_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(allow_button)
        )
        driver.find_element(*allow_button).click()
        logger.info("Clicked on 'Allow' button for notification permission.")
    except TimeoutException:
        logger.info("No notification permission modal displayed, continuing.")

    # ورود به سیستم

    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)

    biometric_page = login_page.click_login()

    # بستن صفحه بیومتریک (در صورت نمایش)
    try:
        biometric_page.confirm_button()
        logger.info("Clicked on 'Allow' button for notification permission.")
    except TimeoutException:
        logger.info("No biometric_page permission modal displayed, continuing.")

    # بررسی دسترسی نوتیفیکیشن (Allow)
    try:
        allow_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(allow_button)
        )
        driver.find_element(*allow_button).click()
        logger.info("Clicked on 'Allow' button for notification permission.")
    except TimeoutException:
        logger.info("No notification permission modal displayed, continuing.")

    # هدایت به داشبورد
    dashboard_page = DashboardPage(driver)
    dashboard_page.device_name = device_name  # اضافه کردن device_name به dashboard_page

    try:
        dashboard_identifier = (AppiumBy.ID, "com.samanpr.blu.dev:id/toolbarTitleTextView")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(dashboard_identifier)
        )
        logger.info("Dashboard page displayed successfully.")
    except TimeoutException:
        logger.error("Failed to load the dashboard page.")

    yield driver, dashboard_page

    driver.quit()
    service.stop()


@pytest.fixture(scope="function")
def driver(request):
    logger.info(f"Starting WebDriver for device: {device_name} with UDID: {device_udid}")

    device_name = request.config.getoption("--device_name")
    device_udid = request.config.getoption("--device_udid")

    desired_caps = {
        "platformName": device_configs[device_name]["platformName"],
        "deviceName": device_name,
        "udid": device_udid,
        "appPackage": device_configs[device_name]["appPackage"],
        "appActivity": device_configs[device_name]["appActivity"],
        "automationName": device_configs[device_name]["automationName"]
    }
    logger.info(f"Desired Capabilities: {desired_caps}")

    try:
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    except Exception as e:
        logger.error(f"Failed to start WebDriver: {e}")
        raise
    yield driver
    driver.quit()


@pytest.fixture
def login_and_dashboard_with_confirmed_user(request):
    from pages.login_page import LoginPage

    # بارگذاری لیست کاربران تأیید شده
    try:
        accounts = load_confirmed_accounts()
        if not accounts:
            raise ValueError("No confirmed accounts available in the file.")
    except FileNotFoundError as e:
        logger.error(f"Confirmed accounts file not found: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading confirmed accounts: {e}")
        raise

        # بارگذاری لیست کاربران تأیید شده
    accounts = load_confirmed_accounts()
    if not accounts:
        raise ValueError("No confirmed accounts available in the file.")

    # انتخاب یک کاربر از لیست
    selected_account = accounts[0]
    username = selected_account['username']

    device_name = request.config.getoption("--device_name")
    options = AppiumOptions()
    options.load_capabilities(device_configs[device_name])

    service = AppiumService()
    service.start()
    appium_url = "http://127.0.0.1:4723"
    driver = webdriver.Remote(appium_url, options=options)

    test_successful = False  # متغیر برای بررسی موفقیت تست
    try:
        allow_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(allow_button)
        )
        driver.find_element(*allow_button).click()
        logger.info("Clicked on 'Allow' button for notification permission.")
    except TimeoutException:
        logger.info("No notification permission modal displayed, continuing.")

    with allure.step("Click on 'has Account' button"):
        try:
            logger.info("کلیک روی دکمه 'حساب کاربری دارم'...")
            has_account_button = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/hasAccountButton"))
            )
            has_account_button.click()
            logger.info("دکمه 'حساب کاربری دارم' کلیک شد.")
        except TimeoutException:
            logger.info("No Create Account button displayed, continuing.")

    # بررسی دسترسی نوتیفیکیشن (Allow)
    try:
        allow_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(allow_button)
        )
        driver.find_element(*allow_button).click()
        logger.info("Clicked on 'Allow' button for notification permission.")
    except TimeoutException:
        logger.info("No notification permission modal displayed, continuing.")

        # ورود به سیستم
        with allure.step("Log in with confirmed user"):
            logger.info(f"Logging in with username: {username}")
            login_page = LoginPage(driver)
            login_page.enter_username(username)
            login_page.enter_password("Aa123456")  # فرض کنید رمز عبور ثابت است

            biometric_page = login_page.click_login()

            # بستن صفحه بیومتریک (در صورت نمایش)
            not_now_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/btnNotNow")
            try:
                WebDriverWait(driver, 2).until(
                    EC.visibility_of_element_located(not_now_button)
                )
                biometric_page.click_not_now()
                logger.info("Clicked on 'Not Now' button in biometric page.")
            except TimeoutException:
                logger.info("No biometric page displayed, skipping.")

        test_successful = True  # اگر همه مراحل بدون خطا انجام شود، تست موفق است
        # بازگرداندن `driver` و `username`
        yield driver, username
    finally:
        # متوقف کردن درایور و سرویس
        driver.quit()
        service.stop()
