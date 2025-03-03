import json
import logging
import pytest
import os
from devices.device_config import device_configs


# تنظیمات و پیکربندی لاگر
def configure_logger():
    """
    این تابع برای تنظیم و پیکربندی لاگر (Logger) استفاده می‌شود.
    - اگر لاگر قبلاً تنظیم نشده باشد، یک لاگر جدید تنظیم می‌کند.
    - فرمت لاگ‌ها شامل زمان، نام ماژول، سطح لاگ و پیام است.
    - لاگ‌ها در دو محل نمایش داده می‌شوند:
        1. در کنسول (StreamHandler)
        2. در یک فایل به نام "test_log.log" (FileHandler)
    """
    logger = logging.getLogger(__name__)  # ایجاد یا دریافت لاگر با نام ماژول
    if not logger.hasHandlers():  # بررسی اینکه آیا هندلری قبلاً تنظیم شده است یا نه
        logging.basicConfig(
            level=logging.INFO,  # سطح پیش‌فرض لاگ‌ها (اینجا INFO)
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # فرمت لاگ‌ها
            handlers=[
                logging.StreamHandler(),  # نمایش لاگ‌ها در کنسول
                logging.FileHandler("test_log.log")  # ذخیره لاگ‌ها در فایل
            ]
        )
    return logger  # بازگرداندن شی لاگر


# ایجاد یا پیکربندی یک لاگر سراسری
logger = logging.getLogger(__name__)  # ایجاد لاگر با نام ماژول
if not logger.hasHandlers():  # بررسی وجود هندلر
    logging.basicConfig(level=logging.INFO)  # تنظیم سطح پیش‌فرض برای لاگر
    logger.setLevel(logging.INFO)  # اطمینان از تنظیم سطح INFO


def capture_screenshot(driver, name="screenshot"):
    """
    این تابع برای گرفتن اسکرین‌شات از وضعیت فعلی درایور و ذخیره آن در یک مسیر مشخص استفاده می‌شود.

    پارامترها:
        - driver: درایور وب (مانند Selenium WebDriver) که وضعیت فعلی صفحه را مدیریت می‌کند.
        - name (اختیاری): نام فایل اسکرین‌شات. پیش‌فرض "screenshot".

    عملیات:
        1. پوشه‌ای به نام `screenshots` ایجاد می‌کند (اگر وجود نداشته باشد).
        2. اسکرین‌شات را با نام مشخص‌شده و پسوند `.png` در مسیر ذخیره می‌کند.
        3. مسیر کامل فایل اسکرین‌شات را برمی‌گرداند.

    خروجی:
        - مسیر فایل اسکرین‌شات که ذخیره شده است.

    مثال:
        capture_screenshot(driver, name="error_page")
        >> فایل `screenshots/error_page.png` در سیستم ذخیره می‌شود.
    """
    # ایجاد پوشه `screenshots` در صورت عدم وجود
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # ذخیره اسکرین‌شات در مسیر مشخص‌شده
    screenshot_path = os.path.join("screenshots", f"{name}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path


def load_test_order(file_path):
    """
    این تابع برای بارگذاری ترتیب تست‌ها از یک فایل JSON استفاده می‌شود.

    پارامترها:
        - file_path: مسیر فایل JSON که ترتیب تست‌ها را ذخیره کرده است.

    عملیات:
        1. بررسی می‌کند که فایل در مسیر مشخص‌شده وجود دارد. اگر وجود نداشته باشد:
            - یک پیام خطا در لاگ ثبت می‌کند.
            - یک استثناء `FileNotFoundError` را مطرح می‌کند.
        2. اگر فایل موجود باشد، محتوای آن را بارگذاری و به‌صورت یک دیکشنری بازمی‌گرداند.

    خروجی:
        - دیکشنری شامل اطلاعات ترتیب تست‌ها.


    استثناء:
        - FileNotFoundError: اگر فایل موجود نباشد.
    """
    if not os.path.exists(file_path):
        logger.error(f"Test order file '{file_path}' not found.")
        raise FileNotFoundError(f"Test order file '{file_path}' not found.")
    with open(file_path, "r") as file:
        return json.load(file)


def run_tests_for_device(device_name):
    """
    این تابع برای اجرای تست‌ها برای یک دستگاه خاص استفاده می‌شود.

    پارامترها:
        - device_name: نام دستگاهی که تست‌ها باید روی آن اجرا شوند.

    عملیات:
        1. بارگذاری ترتیب تست‌ها از فایل JSON (مثلاً `test_order.json`).
        2. بررسی وجود تنظیمات دستگاه در فایل ترتیب تست‌ها:
            - اگر دستگاه وجود نداشته باشد، پیامی به لاگر ارسال می‌شود و عملیات متوقف می‌شود.
        3. استخراج و بررسی لیست تست‌های فعال برای دستگاه:
            - فقط فایل‌هایی که وجود دارند و فعال هستند (enabled=True) به لیست اضافه می‌شوند.
        4. اگر تست معتبری وجود نداشته باشد، عملیات متوقف می‌شود.
        5. ایجاد پوشه‌ای برای ذخیره گزارش‌ها (در صورت نیاز).
        6. تنظیم مسیر گزارش نهایی HTML برای دستگاه.
        7. اجرای pytest با آرگومان‌های مشخص‌شده (شامل نام دستگاه، `udid` و مسیر گزارش).

    خروجی:
        - گزارشی HTML در پوشه `report` که شامل نتایج تست‌ها برای دستگاه مشخص‌شده است.

    مثال:
        run_tests_for_device("Galaxy S24 Ultra")
        >> اجرای تست‌های فعال برای دستگاه "Galaxy S24 Ultra" و ذخیره گزارش در مسیر مشخص‌شده.

    استثناء:
        - اگر فایل‌های تست معتبر نباشند، هیچ تستی اجرا نمی‌شود.
        - اگر دستگاه در فایل ترتیب تست‌ها وجود نداشته باشد، هیچ عملیاتی انجام نمی‌شود.
    """
    # بارگذاری ترتیب تست‌ها از فایل
    test_order = load_test_order("test_order.json")

    # تنظیمات دستگاه انتخاب شده
    if device_name not in test_order["devices"]:
        logger.error(f"Device '{device_name}' not found in test order.")
        return

    device_config = device_configs.get(device_name, {})
    tests = test_order["devices"][device_name]

    # بررسی وجود تست‌ها برای دستگاه
    if not tests:
        logger.warning(f"No tests found for device '{device_name}'")
        return

    # ساخت لیستی از فایل‌های تست برای اجرا در یک pytest
    test_files = [
        test["file"] for test in tests
        if os.path.exists(test["file"]) and test.get("enabled", True)  # چک کردن 'enabled'
    ]

    # اضافه کردن لاگ تعداد تست‌ها
    logger.info(f"Found {len(test_files)} test(s) for device '{device_name}':\n" + "\n".join(test_files))

    if not test_files:
        logger.error(f"No valid test files found for device '{device_name}'")
        return

    # ایجاد پوشه 'report' اگر وجود ندارد
    report_dir = os.path.join(os.getcwd(), 'report')
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # تنظیم مسیر گزارش نهایی برای هر دستگاه
    report_file = os.path.join(report_dir, f"report_{device_name}.html")

    pytest_args = [
        *test_files,  # لیست فایل‌های تست
        "-v",  # برای نمایش اطلاعات بیشتر
        f"--device_name={device_name}",
        f"--device_udid={device_config.get('udid', 'unknown_udid')}",  # تنظیم پیش‌فرض برای udid
        f"--html={report_file}",  # تولید گزارش HTML در مسیر جدید
        "--self-contained-html",  # ایجاد گزارش مستقل HTML
    ]
    try:
        pytest.main(pytest_args)
    except Exception as e:
        logger.error(f"Error occurred during pytest execution: {e}")
