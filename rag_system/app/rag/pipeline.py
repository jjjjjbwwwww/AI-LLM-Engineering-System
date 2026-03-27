# app/rag/pipeline.py

from .hybrid_retriever import HybridRetriever
from .fusion import fuse
from .reranker import Reranker
from .rewrite import QueryRewriter
from .generator import Generator
from .fallback import Fallback
from .evaluator import Evaluator

class RAGPipeline:

    def __init__(self):
        self.retriever = HybridRetriever()
        self.reranker = Reranker()
        self.rewriter = QueryRewriter()
        self.generator = Generator()
        self.fallback = Fallback()
        self.evaluator = Evaluator()

    def run(self, query):
        # 1. 改写
        new_query = self.rewriter.rewrite(query)

        # 2. 多路召回
        v_docs, b_docs = self.retriever.retrieve(new_query)

        # 3. 融合
        docs = fuse(v_docs, b_docs)

        if not docs:
            return self.fallback.run(query)

        # 4. rerank
        docs = self.reranker.rerank(new_query, docs)

        # 5. context
        context = "\n".join([doc.page_content for doc in docs])

        # 6. 生成
        answer = self.generator.generate(query, context)

        # 7. 评估
        ok = self.evaluator.evaluate(query, answer)

        if not ok:
            return self.fallback.run(query)

        return answer