import os
import logging

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "system.log")

# التأكد من وجود مجلد السجلات
os.makedirs(LOG_DIR, exist_ok=True)

# إعداد نظام التسجيل (Logging)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def log_event(status, message):
    """
    تسجيل الأحداث مع حالتها (مثل SUCCESS أو FAILED)
    """
    log_msg = f"[{status}] {message}"
    if status == "SUCCESS" or status == "VALIDATION_PASSED":
        logging.info(log_msg)
    elif status == "WARNING":
        logging.warning(log_msg)
    else:
        logging.error(log_msg)