

from langchain_openai import ChatOpenAI

class Fallback:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")

    def run(self, query):
        return self.llm.invoke(query).content