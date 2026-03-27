
from langchain_openai import ChatOpenAI

class Fixer:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")

    def fix(self, code, error):
        prompt = f"""
请修复以下Python代码：

代码：
{code}

错误：
{error}

输出完整修复后的代码：
"""
        return self.llm.invoke(prompt).content