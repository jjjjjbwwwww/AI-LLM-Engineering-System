
## Enterprise RAG v2（企业级检索增强生成系统）
## 项目简介

本项目实现了一个具备 多路召回 + 重排序 + 自动评估 + 兜底机制 的企业级 RAG 系统，解决大模型幻觉与不稳定问题。

## 核心能力
✅ Query Rewrite（查询优化）
✅ Hybrid Retrieval（向量 + BM25）
✅ Rerank（CrossEncoder精排）
✅ Answer Evaluation（自动评估）
✅ Fallback机制（兜底策略）
## 系统架构
用户问题
→ Query Rewrite
→ 多路召回（Vector + BM25）
→ Fusion融合
→ Rerank排序
→ Context构建
→ LLM生成
→ Answer Eval
→ Fallback
## 项目结构
rag-system/
│
├── app/
│   ├── main.py
│   ├── rag/
│   │   ├── pipeline.py
│   │   ├── hybrid_retriever.py
│   │   ├── reranker.py
│   │   ├── rewrite.py
│   │   ├── generator.py
│   │   ├── fallback.py
│   │   └── evaluator.py
│
├── scripts/
│   └── ingest.py
│
├── data/
├── requirements.txt
└── README.md
## 安装依赖
pip install fastapi uvicorn langchain faiss-cpu sentence-transformers openai rank-bm25
## 数据入库
python scripts/ingest.py
## 启动服务
uvicorn app.main:app --reload

接口：

GET /ask?query=你的问题
## 核心设计
1️⃣ 多路召回（Hybrid Retrieval）
向量检索：语义匹配
BM25：关键词匹配
提高召回率
2️⃣ Rerank（重排序）
使用CrossEncoder进行精排
提升上下文质量
3️⃣ Query Rewrite
优化用户输入
提高检索命中率
4️⃣ 自动评估（Eval）
使用LLM判断答案质量
过滤低质量输出
5️⃣ Fallback机制
检索失败或低质量答案 → LLM直答
保证系统可用性
## 系统优势
高召回（Hybrid Retrieval）
高精度（Rerank）
高可靠（Eval + Fallback）
## 风险控制
降低幻觉（RAG + Eval）
提高稳定性（Fallback）
控制输出质量