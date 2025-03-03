import os
import subprocess

from utils.utils import logger  # وارد کردن لاگر برای ثبت گزارش‌ها
from utils.config import run_tests_for_device  # تابع اجرای تست‌ها برای دستگاه


def restart_allure_server():
    try:
        # ابتدا هر سرور Allure قبلی را متوقف کنید
        os.system("taskkill /F /IM java.exe")  # اگر روی ویندوز هستید
        # اگر روی لینوکس/مک هستید:
        # os.system("pkill -f allure")

        # اجرای مجدد سرور Allure
        subprocess.Popen(["allure", "serve", "allure-results"], shell=True)
        logger.info("Allure server restarted successfully.")
    except Exception as e:
        logger.error(f"Failed to restart Allure server: {e}")


if __name__ == "__main__":
    devices = ["Galaxy S24 Ultra"]  # لیست دستگاه‌ها
    for device in devices:
        logger.info(f"Running tests on {device}...")
        run_tests_for_device(device)

    # ری‌استارت کردن سرور Allure بعد از اجرای تست‌ها
    restart_allure_server()

################################اجرای تست‌ها به‌صورت موازی (Parallel)######################################
#
# import json
# import os
# import logging
# import subprocess
# from multiprocessing import Process
# import pytest
#
# # تنظیم لاگر
# logger = logging.getLogger(__name__)
# if not logger.hasHandlers():
#     logging.basicConfig(level=logging.INFO)
#     logger.setLevel(logging.INFO)
#
#
# def load_test_order(file_path):
#     """خواندن ترتیب تست‌ها از فایل JSON"""
#     if not os.path.exists(file_path):
#         logger.error(f"Test order file '{file_path}' not found.")
#         raise FileNotFoundError(f"Test order file '{file_path}' not found.")
#     with open(file_path, "r", encoding="utf-8") as file:
#         return json.load(file)
#
#
# def run_tests_for_device(device_name):
#     """اجرای تست‌ها برای دستگاه مشخص"""
#     try:
#         # بارگذاری ترتیب تست‌ها
#         test_order = load_test_order("test_order.json")
#
#         # تنظیمات دستگاه
#         if device_name not in test_order["devices"]:
#             logger.error(f"Device '{device_name}' not found in test order.")
#             return
#
#         # فیلتر کردن فقط تست‌هایی که enabled=true هستند
#         device_tests = [
#             test["file"]
#             for test in test_order["devices"][device_name]
#             if test.get("enabled", False) and os.path.exists(test["file"])
#         ]
#
#         if not device_tests:
#             logger.warning(f"No enabled tests found for device '{device_name}'")
#             return
#
#         # گزارش تست برای دستگاه
#         report_file = f"report_{device_name.replace(' ', '_')}.html"
#
#         # تنظیمات pytest
#         pytest_args = [
#             *device_tests,  # لیست فایل‌های تست
#             "-v",  # نمایش لاگ‌های تست
#             f"--device_name={device_name}",
#             f"--html={report_file}",  # گزارش HTML
#             "--self-contained-html",  # گزارش مستقل
#         ]
#
#         # اجرای تست‌ها با pytest
#         logger.info(f"Running tests for device: {device_name}")
#         pytest.main(pytest_args)
#
#     except Exception as e:
#         logger.error(f"Error running tests for device '{device_name}': {e}")
#
#
# def restart_allure_server():
#     try:
#         # ابتدا هر سرور Allure قبلی را متوقف کنید
#         os.system("taskkill /F /IM java.exe")  # اگر روی ویندوز هستید
#         # اگر روی لینوکس/مک هستید:
#         # os.system("pkill -f allure")
#
#         # اجرای مجدد سرور Allure
#         subprocess.Popen(["allure", "serve", "allure-results"], shell=True)
#         logger.info("Allure server restarted successfully.")
#     except Exception as e:
#         logger.error(f"Failed to restart Allure server: {e}")
#
#
# if __name__ == "__main__":
#     # لیست دستگاه‌ها برای تست
#     devices = ["Galaxy S24 Ultra", "pixel 8"]
#
#     # ایجاد پروسه برای هر دستگاه
#     processes = []
#     for device in devices:
#         p = Process(target=run_tests_for_device, args=(device,))
#         processes.append(p)
#         p.start()
#
#     # منتظر ماندن برای اتمام همه پروسه‌ها
#     for p in processes:
#         p.join()
#
#     logger.info("All tests completed.")
#
#     # ری‌استارت کردن سرور Allure بعد از اجرای تست‌ها
#     restart_allure_server()
