import os
import chromadb
from src.logger import log_event

DB_PATH = "chroma_db"

def get_vector_database():
    """
    إعداد وإنشاء الاتصال بقاعدة بيانات ChromaDB المحلية
    """
    try:
        os.makedirs(DB_PATH, exist_ok=True)
        client = chromadb.PersistentClient(path=DB_PATH)
        # إنشاء أو استرجاع مجموعة بيانات الجامعة
        collection = client.get_or_create_collection(name="university_knowledge_base")
        log_event("SUCCESS", "Successfully connected to ChromaDB vector database.")
        return collection
    except Exception as e:
        log_event("ERROR", f"Failed to initialize vector database: {str(e)}")
        return None

def add_chunks_to_db(chunks, embeddings, metadatas=None):
    """
    إضافة الأجزاء المتجهية مع نصوصها إلى قاعدة البيانات
    """
    collection = get_vector_database()
    if not collection:
        return False

    try:
        ids = [str(i) for i in range(len(chunks))]
        if metadatas is None:
            metadatas = [{"source": "academic_faq.txt"} for _ in chunks]

        collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        log_event("SUCCESS", f"Added {len(chunks)} chunks to ChromaDB successfully.")
        return True
    except Exception as e:
        log_event("ERROR", f"Failed to add chunks to vector database: {str(e)}")
        return False