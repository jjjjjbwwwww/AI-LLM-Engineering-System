
from langchain_openai import ChatOpenAI

class QueryRewriter:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")

    def rewrite(self, query):
        prompt = f"""
请优化用户问题，使其更适合检索：
原问题：{query}
优化后：
"""
        result = self.llm.invoke(prompt)
        return result.content.strip()