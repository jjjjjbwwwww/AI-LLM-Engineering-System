
# app/main.py

from fastapi import FastAPI
from app.rag.pipeline import RAGPipeline

app = FastAPI()
rag = RAGPipeline()

@app.get("/ask")
def ask(query: str):
    answer = rag.run(query)
    return {"answer": answer}