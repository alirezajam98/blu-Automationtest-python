import json
import os
import random
import logging
import re
from pathlib import Path

import jdatetime
from jdatetime import datetime as jdatetime_datetime

import allure

from utils.config import capture_screenshot

# تنظیم لاگر برای نمایش فقط لاگ‌های INFO و ERROR
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def check_text_match(actual, expected, description, driver=None, critical=False):
    """
    بررسی تطابق متن‌ها و ثبت خطاها با گرفتن اسکرین‌شات در صورت عدم تطابق.

    پارامترها:
    - actual: مقدار واقعی.
    - expected: مقدار مورد انتظار.
    - description: توضیح خطا.
    - driver: درایور برای گرفتن اسکرین‌شات در صورت خطا (اختیاری).
        - critical: اگر True باشد، تست در صورت خطا متوقف می‌شود.

    """
    try:
        assert actual == expected, f"Expected '{expected}', but got '{actual}'"
        logger.info(f"{description}: {actual}")
    except AssertionError as e:
        logger.error(f"{description} - {e}")
        allure.attach(f"Expected: {expected}\nActual: {actual}", f"{description} Mismatch", allure.attachment_type.TEXT)

        # گرفتن اسکرین‌شات در صورت وجود درایور
        if driver:
            screenshot_path = capture_screenshot(driver, description.replace(" ", "_"))
            allure.attach.file(screenshot_path, name=f"{description} Screenshot",
                               attachment_type=allure.attachment_type.PNG)

        if critical:
            # اگر مقدار critical True باشد، خطا را raise می‌کنیم و تست متوقف می‌شود
            raise e


def mobile_number_generator():
    """
    تولید یک شماره موبایل تصادفی که با پیشوند 091 شروع می‌شود.
    این تابع 8 رقم تصادفی تولید کرده و به پیشوند 091 اضافه می‌کند.

    خروجی:
        mobile_number (str): شماره موبایل تولید شده.
    """
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    mobile_number = "091" + random_digits
    return mobile_number


def national_code_generator():
    """
    تولید یک کد ملی معتبر به صورت تصادفی.
    کد ملی تولید شده دارای 10 رقم است که رقم آخر آن با استفاده از الگوریتم کنترل محاسبه می‌شود.

    خروجی:
        national_code (str): کد ملی معتبر تولید شده.
    """
    number_list, sum_digits = [], 0
    for i in range(10, 1, -1):
        j = random.randint(0, 9)  # تولید یک رقم تصادفی
        number_list.append(j)  # افزودن رقم به لیست
        sum_digits += j * i  # محاسبه مجموع ارقام ضرب شده در وزن‌های مربوطه

    # محاسبه رقم کنترل (Check Digit)
    number_list.append(sum_digits % 11 if sum_digits % 11 < 2 else 11 - sum_digits % 11)

    return ''.join(map(str, number_list))  # تبدیل لیست اعداد به رشته


def read_counter(filename='utils/counter.txt'):
    """
    خواندن مقدار شمارنده از فایل.

    پارامترها:
        filename (str): مسیر فایل شمارنده. (پیش‌فرض: 'utils/counter.txt')

    خروجی:
        counter (int): مقدار فعلی شمارنده. اگر فایل وجود نداشته باشد، مقدار 0 بازگردانده می‌شود.
    """
    return int(open(filename).read().strip()) if os.path.exists(filename) else 0


def write_counter(counter, filename='utils/counter.txt'):
    """
    ذخیره مقدار شمارنده در فایل.

    پارامترها:
        counter (int): مقدار شمارنده برای ذخیره‌سازی.
        filename (str): مسیر فایل شمارنده. (پیش‌فرض: 'utils/counter.txt')
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # ایجاد پوشه در صورت عدم وجود
    with open(filename, 'w') as file:
        file.write(str(counter))


def username_generator():
    """
    تولید یک نام کاربری یکتا با استفاده از شمارنده ذخیره شده در فایل.
    هر بار که تابع فراخوانی می‌شود، شمارنده افزایش یافته و نام کاربری جدیدی تولید می‌شود.

    خروجی:
        username (str): نام کاربری تولید شده.
    """
    counter = read_counter() + 1  # افزایش مقدار شمارنده
    write_counter(counter)  # ذخیره مقدار جدید در فایل
    return f"boxtest{counter}"  # بازگرداندن نام کاربری با قالب دلخواه


def save_account_to_file(username, file_path='utils/confirmed_accounts.json'):
    """
    ذخیره نام کاربری در فایل JSON.

    اگر فایل وجود نداشته باشد، به صورت خودکار ایجاد می‌شود.
    سپس نام کاربری جدید به لیست موجود در فایل اضافه شده و فایل به‌روزرسانی می‌شود.

    پارامترها:
        username (str): نام کاربری که باید ذخیره شود.
        file_path (str): مسیر فایل ذخیره‌سازی کاربران تأیید شده (پیش‌فرض: 'utils/confirmed_accounts.json').
    """
    # اگر فایل وجود ندارد، ایجاد یک فایل خالی
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)  # ایجاد یک آرایه خالی

    # بارگذاری اطلاعات موجود
    with open(file_path, 'r') as file:
        accounts = json.load(file)

    # افزودن نام کاربری جدید به لیست
    accounts.append({"username": username})
    logger.info(f"Added username '{username}' to the confirmed accounts list. Total accounts: {len(accounts)}")

    # ذخیره اطلاعات به‌روزرسانی شده
    with open(file_path, 'w') as file:
        json.dump(accounts, file, indent=4)


def load_confirmed_accounts(file_path='utils/confirmed_accounts.json'):
    """
    بارگذاری لیست کاربران تأیید شده از فایل JSON.

    اگر فایل وجود نداشته باشد، خطای FileNotFoundError تولید می‌شود.

    پارامترها:
        file_path (str): مسیر فایل ذخیره‌سازی کاربران تأیید شده (پیش‌فرض: 'utils/confirmed_accounts.json').

    خروجی:
        list: لیست کاربران تأیید شده.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        return json.load(file)


def remove_used_account(username, file_path='utils/confirmed_accounts.json'):
    """
    حذف نام کاربری از فایل JSON.

    نام کاربری مشخص شده از لیست کاربران تأیید شده در فایل حذف شده و تغییرات ذخیره می‌شود.
    اگر فایل وجود نداشته باشد، خطای FileNotFoundError تولید می‌شود.

    پارامترها:
        username (str): نام کاربری که باید حذف شود.
        file_path (str): مسیر فایل ذخیره‌سازی کاربران تأیید شده (پیش‌فرض: 'utils/confirmed_accounts.json').
    """
    # بررسی وجود فایل
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # بارگذاری لیست کاربران
    with open(file_path, 'r') as file:
        accounts = json.load(file)

    # حذف کاربر مورد نظر
    accounts = [account for account in accounts if account['username'] != username]

    # ذخیره تغییرات به فایل
    with open(file_path, 'w') as file:
        json.dump(accounts, file, indent=4)

    logger.info(f"User '{username}' has been removed from the confirmed accounts list.")


def convert_persian_to_english_numbers(text):
    """
    تبدیل اعداد فارسی به اعداد لاتین
    """
    persian_to_english = str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789')
    return text.translate(persian_to_english)


def normalize_card_number(card_number):
    """
    حذف تمام کاراکترهای غیرعددی و تبدیل اعداد فارسی به لاتین
    """
    # تبدیل اعداد فارسی به لاتین
    card_number = convert_persian_to_english_numbers(card_number)
    # حذف تمامی کاراکترهای غیرعددی
    return re.sub(r'\D', '', card_number)


def is_six_digit_persian_number(text):
    """
    بررسی می‌کند که آیا متن ورودی یک عدد فارسی ۶ رقمی است یا خیر.
    """
    pattern = r'^[۰-۹]{6}$'  # الگوی عدد فارسی با ۶ رقم
    return bool(re.match(pattern, text))


def get_today_date():
    today = jdatetime_datetime.now()
    # تبدیل اعداد انگلیسی به فارسی
    persian_numbers = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }
    date_str = today.strftime('%Y/%m/%d')  # تاریخ به صورت انگلیسی
    # تبدیل اعداد به فارسی
    for eng, fa in persian_numbers.items():
        date_str = date_str.replace(eng, fa)
    return date_str


def get_date_18_years_ago():
    # تاریخ امروز
    today = jdatetime_datetime.now()
    # محاسبه تاریخ ۱۸ سال پیش
    date_18_years_ago = today.replace(year=today.year - 18)
    # تبدیل اعداد انگلیسی به فارسی
    persian_numbers = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }
    date_str = date_18_years_ago.strftime('%Y/%m/%d')  # تاریخ به صورت انگلیسی
    # تبدیل اعداد به فارسی
    for eng, fa in persian_numbers.items():
        date_str = date_str.replace(eng, fa)
    return date_str


def load_accounts():
    try:
        file_path = Path(__file__).parent / "accounts.json"
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise RuntimeError("File accounts.json not found!")
    except json.JSONDecodeError:
        raise RuntimeError("Invalid JSON format in accounts.json!")


def update_accounts(username, new_pass1, new_pass2):
    try:
        file_path = Path("utils/accounts.json")
        with open(file_path, "r", encoding="utf-8") as f:
            accounts = json.load(f)

        # به‌روزرسانی پسوردها
        if username in accounts:
            accounts[username]["pass1"] = new_pass1
            accounts[username]["pass2"] = new_pass2

        # ذخیره تغییرات در فایل
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(accounts, f, indent=4)
        logger.info(f"Updated passwords for user '{username}' in accounts.json.")
    except FileNotFoundError:
        raise RuntimeError("File accounts.json not found!")
    except json.JSONDecodeError:
        raise RuntimeError("Invalid JSON format in accounts.json!")