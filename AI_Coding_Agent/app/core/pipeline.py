

import os
from app.agents.generator import CodeGenerator
from app.agents.debugger import Debugger
from app.agents.fixer import Fixer
from app.tools.runner import run_code

WORKSPACE = "workspace/code.py"

class CodingAgent:

    def __init__(self):
        self.generator = CodeGenerator()
        self.debugger = Debugger()
        self.fixer = Fixer()

    def run(self, task, max_iter=3):
        code = self.generator.generate(task)

        for i in range(max_iter):
            # 写入文件
            with open(WORKSPACE, "w", encoding="utf-8") as f:
                f.write(code)

            stdout, stderr = run_code(WORKSPACE)

            if not stderr:
                return {
                    "success": True,
                    "code": code,
                    "output": stdout
                }

            # 分析错误
            analysis = self.debugger.analyze(code, stderr)

            # 修复代码
            code = self.fixer.fix(code, stderr)

        return {
            "success": False,
            "code": code,
            "error": stderr
        }