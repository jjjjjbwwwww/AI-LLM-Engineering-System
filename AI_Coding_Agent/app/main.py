# app/main.py

from fastapi import FastAPI
from app.core.pipeline import CodingAgent

app = FastAPI()
agent = CodingAgent()

@app.get("/code")
def generate(task: str):
    return agent.run(task)