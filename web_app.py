import streamlit as st
import os
from src.rag_pipeline import run_rag_query, run_ingestion_pipeline

st.title("🎓 University RAG Assistant")

# 1. File Upload Section in Sidebar
st.sidebar.header("Upload New Data")
uploaded_file = st.sidebar.file_uploader("Choose a text file (.txt)", type=["txt"])

if uploaded_file is not None:
    # Save the file to the documents folder
    save_path = os.path.join("data/documents", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Run ingestion pipeline for the new file
    if run_ingestion_pipeline(save_path):
        st.sidebar.success(f"Successfully uploaded and indexed: {uploaded_file.name}")

# 2. Search / Query Section
st.write("Ask any question regarding the academic systems and courses:")
user_query = st.text_input("Type your question here:")

if user_query:
    with st.spinner("Searching..."):
        answer = run_rag_query(user_query)
        st.success("Answer:")
        st.write(answer)