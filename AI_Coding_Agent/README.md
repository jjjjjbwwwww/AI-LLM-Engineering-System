
AI Coding Agent（代码生成 + 自动修复系统）
## 项目简介

本项目实现了一个具备 代码生成 → 执行 → 错误分析 → 自动修复 的闭环 AI 系统，使大模型从“写代码”进化为“具备调试能力的开发助手”。

## 核心能力
1 自动生成 Python 代码
2 执行代码并获取真实运行结果
3 分析报错（LLM Debug）
4 自动修复代码（迭代优化）
5 构建完整开发闭环
🏗️ 系统架构
用户需求
→ Code Generator（代码生成）
→ Runner（执行代码）
→ Debugger（错误分析）
→ Fixer（自动修复）
→ 循环迭代（直到成功）
## 项目结构
coding-agent/
│
├── app/
│   ├── main.py
│   ├── agents/
│   │   ├── generator.py
│   │   ├── debugger.py
│   │   ├── fixer.py
│   │
│   ├── core/
│   │   └── pipeline.py
│   │
│   ├── tools/
│   │   └── runner.py
│
├── workspace/
├── requirements.txt
└── README.md
## 安装依赖
pip install fastapi uvicorn langchain openai
## 运行项目
uvicorn app.main:app --reload

## 访问接口：

GET /code?task=写一个快速排序
## 核心设计
1️⃣ 生成-执行-反馈-修复闭环
避免“一次生成错误代码”
提升代码正确率
2️⃣ Debug能力
不直接重写代码
先分析错误原因，再修复
3️⃣ 自动迭代
支持多轮修复
设置最大迭代次数防止死循环
## 安全设计
执行超时控制
限制执行环境（建议后续沙箱化）
禁止危险系统命令（可扩展）
## 可扩展方向
引入测试用例（单元测试）
支持多语言（JS / Java）
集成IDE（如Cursor）
 