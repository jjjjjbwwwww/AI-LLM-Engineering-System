# app/rag/evaluator.py

from langchain_openai import ChatOpenAI

class Evaluator:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")

    def evaluate(self, query, answer):
        prompt = f"""
判断下面回答是否合理：

问题：{query}
回答：{answer}

请输出：
score: 0-1
reason:
"""
        res = self.llm.invoke(prompt).content

        if "score: 1" in res or "score: 0.9" in res:
            return True
        return False