from src.logger import log_event

def chunk_text(text, chunk_size=500, chunk_overlap=50):
    """
    أصغر لتسهيل البحث واسترجاع المعلومات (Chunks) تقسيم النص الطويل إلى أجزاء
    """
    if not text:
        log_event("WARNING", "Attempted to chunk empty text.")
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - chunk_overlap

    log_event("SUCCESS", f"Successfully split text into {len(chunks)} chunks.")
    return chunks