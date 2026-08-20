import os
from src.logger import log_event

def load_document(file_path):
    """
    تحميل قراءة محتوى الملفات النصية أو ملفات الـ FAQ
    """
    if not os.path.exists(file_path):
        log_event("ERROR", f"File not found for loading: {file_path}")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        log_event("SUCCESS", f"Successfully loaded document: {os.path.basename(file_path)}")
        return content
    except Exception as e:
        log_event("ERROR", f"Failed to load document {file_path}: {str(e)}")
        return None