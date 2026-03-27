

from langchain_openai import ChatOpenAI

class Debugger:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")

    def analyze(self, code, error):
        prompt = f"""
以下代码报错：

代码：
{code}

错误：
{error}

请分析错误原因：
"""
        return self.llm.invoke(prompt).content