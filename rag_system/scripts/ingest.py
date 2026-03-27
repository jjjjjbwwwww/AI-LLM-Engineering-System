
# scripts/ingest.py

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

DATA_PATH = "../data"

def load_docs():
    docs = []
    for file in os.listdir(DATA_PATH):
        with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.create_documents(docs)

def build_vectorstore(docs):
    embedding = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs, embedding)
    db.save_local("faiss_index")

if __name__ == "__main__":
    docs = load_docs()
    chunks = split_docs(docs)
    build_vectorstore(chunks)