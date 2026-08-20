from src.embeddings import generate_embeddings
from src.vector_database import get_vector_database
from src.logger import log_event

def search_knowledge_base(query, n_results=2):
    """
    البحث عن أفضل الأجزاء (Chunks) المطابقة لسؤال المستخدم داخل قاعدة البيانات المتجهية
    """
    collection = get_vector_database()
    if not collection:
        return []

    try:
        # توليد Embedding لسؤال المستخدم
        query_embedding = generate_embeddings([query])
        if not query_embedding:
            return []

        # البحث في قاعدة البيانات عن أقرب النصوص تشابهاً
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        
        retrieved_docs = results.get("documents", [[]])[0]
        log_event("SUCCESS", f"Successfully retrieved {len(retrieved_docs)} documents for query: {query}")
        return retrieved_docs
    except Exception as e:
        log_event("ERROR", f"Failed to search knowledge base: {str(e)}")
        return []