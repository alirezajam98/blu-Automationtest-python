import logging

# تنظیمات logger
logger = logging.getLogger("TestLogger")
logger.setLevel(logging.DEBUG)

# ساخت Handler برای کنسول
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# فرمت لاگ‌ها
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# افزودن Handler به logger
logger.addHandler(console_handler)
