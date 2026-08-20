import os
import hashlib
from src.logger import log_event

SUPPORTED_EXTENSIONS = ['.pdf', '.txt', '.csv', '.xlsx']

def get_file_hash(file_path):
    """حساب بصمة الملف للتأكد من عدم تكراره"""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def validate_document(file_path, existing_hashes=None):
    """
    التحقق من صحة المستند المرفوع وفحص الأخطاء الشائعة
    """
    if existing_hashes is None:
        existing_hashes = set()

    # 1. التحقق من وجود الملف
    if not os.path.exists(file_path):
        log_event("VALIDATION_FAILED", f"File not found: {file_path}")
        return False, "File does not exist."

    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1].lower()

    # 2. التحقق من امتداد الملف
    if file_extension not in SUPPORTED_EXTENSIONS:
        log_event("VALIDATION_FAILED", f"Unsupported extension for {file_name}")
        return False, f"Unsupported file format: {file_extension}. Allowed formats: {SUPPORTED_EXTENSIONS}"

    # 3. التحقق مما إذا كان الملف فارغاً
    if os.path.getsize(file_path) == 0:
        log_event("VALIDATION_FAILED", f"Empty file detected: {file_name}")
        return False, "The uploaded file is empty."

    # 4. التحقق من التكرار عبر بصمة الملف (SHA-256)
    file_hash = get_file_hash(file_path)
    if file_hash in existing_hashes:
        log_event("VALIDATION_FAILED", f"Duplicate file detected: {file_name}")
        return False, "This document has already been uploaded (Duplicate)."

    existing_hashes.add(file_hash)
    log_event("VALIDATION_PASSED", f"File passed validation: {file_name}")
    return True, "Document passed all validation checks."