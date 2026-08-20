import os
os.environ["HF_HOME"] = "D:/huggingface_cache"

from sentence_transformers import SentenceTransformer
from src.logger import log_event

MODEL_NAME = "all-MiniLM-L6-v2"
# ... باقي الكود مثل ما هو
from sentence_transformers import SentenceTransformer
from src.logger import log_event

# استخدام نموذج مجاني ومحلي خفيف وسريع من HuggingFace
MODEL_NAME = "all-MiniLM-L6-v2"

def get_embedding_model():
    """
    تحميل نموذج تحويل النصوص إلى متجهات (Embeddings)
    """
    try:
        model = SentenceTransformer(MODEL_NAME)
        log_event("SUCCESS", f"Loaded embedding model: {MODEL_NAME}")
        return model
    except Exception as e:
        log_event("ERROR", f"Failed to load embedding model: {str(e)}")
        return None

def generate_embeddings(texts):
    """
    توليد المتجهات للنصوص المدخلة
    """
    model = get_embedding_model()
    if not model:
        return []
    
    try:
        embeddings = model.encode(texts).tolist()
        log_event("SUCCESS", f"Generated embeddings for {len(texts)} chunks.")
        return embeddings
    except Exception as e:
        log_event("ERROR", f"Failed to generate embeddings: {str(e)}")
        return []