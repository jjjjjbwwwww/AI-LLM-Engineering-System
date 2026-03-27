## AI LLM Engineering System

##  项目简介

本仓库实现了一套完整的 **大模型应用工程系统（LLM Engineering System）**，涵盖：

*  检索增强生成（RAG）
*  多智能体任务系统（Agent）
*  AI Coding Agent（代码生成与自动修复）
*  LLM Evaluation System（评估与优化闭环）

目标是将大模型从“能力工具”转变为**可控、可评估、可迭代的工程系统**。

---

##  核心能力

* ✅ 构建企业级RAG系统（高召回 + 高精度 + 高可靠）
* ✅ 实现多Agent任务拆解与执行
* ✅ 构建代码生成 + 执行 + Debug闭环
* ✅ 搭建LLM评估系统（Evaluation Loop）
* ✅ 提供系统级优化能力（而非简单调用模型）

---

##  系统整体架构

```text
用户请求
   ↓
AI系统（RAG / Agent / Coding）
   ↓
LLM输出
   ↓
Evaluation System（自动评估）
   ↓
Metrics + Logs
   ↓
Analysis（问题分析）
   ↓
Optimization（优化策略）
```

---

##  项目结构

```bash
.
├── AI_Coding_Agent/        # 💻 代码生成 + 自动修复系统
├── rag_system/             # 🧠 企业级RAG系统（v2）
├── llm_eval_system/        # 📊 LLM评估与优化系统
│
├── requirements.txt        # 统一依赖
├── pyproject.toml          # 项目配置
├── .gitignore
└── README.md
```

---

##  子项目介绍

---

###  AI Coding Agent

> 代码生成 → 执行 → 错误分析 → 自动修复

* 支持自动生成Python代码
* 支持代码执行与错误捕获
* 基于LLM进行错误分析与修复
* 构建完整开发闭环

 路径：`AI_Coding_Agent/`

---

###  Enterprise RAG System（v2）

> 多路召回 + Rerank + Eval + Fallback

* Hybrid Retrieval（向量 + BM25）
* Query Rewrite（查询优化）
* CrossEncoder Rerank
* 自动评估与兜底机制

 路径：`rag_system/`

---

## LLM Evaluation System

> 评估 → 分析 → 优化闭环系统

* LLM-as-Judge 自动评分
* 多维度指标（正确性 / 相关性 / 完整性）
* 日志与指标统计
* 自动分析与优化建议

 路径：`llm_eval_system/`

---

##  安装依赖

```bash
pip install -r requirements.txt
```

---

##  快速运行（示例）

```bash
# 启动RAG系统
uvicorn rag_system.app.main:app --reload

# 启动Coding Agent
uvicorn AI_Coding_Agent.app.main:app --reload

# 启动评估系统
uvicorn llm_eval_system.app.main:app --reload
```

---

##  项目亮点

*  构建完整LLM工程体系（RAG + Agent + Eval）
*  从“调用模型”升级为“控制模型”
*  提供评估与优化闭环（Evaluation Loop）
*  具备企业级系统设计能力

---

##  技术栈

* Python
* FastAPI
* LangChain
* OpenAI API
* FAISS / BM25
* CrossEncoder（Rerank）

---

##  后续优化方向

* 引入缓存与性能优化（KV Cache / Streaming）
* 多Agent协作调度系统
* 自动Prompt优化系统
* 数据闭环（用户反馈 → 模型优化）

---

##  一句话总结

> 本项目将LLM从“不可控生成工具”转变为“可评估、可优化的工程系统”
