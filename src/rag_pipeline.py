from src.document_loader import load_document
from src.chunker import chunk_text
from src.embeddings import generate_embeddings
from src.vector_database import add_chunks_to_db
from src.retriever import search_knowledge_base
from src.llm import generate_rag_response
from src.logger import log_event

def run_ingestion_pipeline(file_path):
    """خطوة إدخال وتخزين البيانات"""
    text = load_document(file_path)
    if text:
        chunks = chunk_text(text)
        embeddings = generate_embeddings(chunks)
        if add_chunks_to_db(chunks, embeddings):
            log_event("SUCCESS", "Ingestion pipeline completed successfully.")
            return True
    return False

def run_rag_query(query):
    """خطوة الاستعلام عن البيانات"""
    contexts = search_knowledge_base(query)
    response = generate_rag_response(query, contexts)
    return response