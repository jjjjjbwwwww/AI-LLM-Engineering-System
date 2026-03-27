
from langchain_openai import ChatOpenAI

class CodeGenerator:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")

    def generate(self, task):
        prompt = f"""
请写一段Python代码实现以下需求：

{task}

要求：
- 可运行
- 完整代码
- 不要解释
"""
        return self.llm.invoke(prompt).content