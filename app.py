from src.rag_pipeline import run_ingestion_pipeline, run_rag_query
import os

file_path = "data/documents/academic_faq.txt"

# تخزين البيانات في قاعدة البيانات المتجهية
print("--- Ingesting Documents ---")
run_ingestion_pipeline(file_path)

# تجربة السؤال
query = "What is the prerequisite for Database Systems (CS301)?"
print(f"\nQuery: {query}")
answer = run_rag_query(query)
print(f"\nResponse:\n{answer}")