# app/rag/hybrid_retriever.py

from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from rank_bm25 import BM25Okapi
import os

class HybridRetriever:

    def __init__(self):
        self.embedding = HuggingFaceEmbeddings()
        self.db = FAISS.load_local("faiss_index", self.embedding)

        # BM25 corpus
        self.docs = [doc.page_content for doc in self.db.docstore._dict.values()]
        tokenized = [doc.split() for doc in self.docs]
        self.bm25 = BM25Okapi(tokenized)

    def vector_search(self, query, k=5):
        return self.db.similarity_search(query, k=k)

    def bm25_search(self, query, k=5):
        scores = self.bm25.get_scores(query.split())
        topk = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        return [self.docs[i] for i in topk]

    def retrieve(self, query):
        v_docs = self.vector_search(query)
        b_docs = self.bm25_search(query)

        return v_docs, b_docs