from lazyllm import Document, Retriever

doc = Document(
    '/home/mnt/dengyuang/workspace/lazy_learn'
)
retriever = Retriever(doc,
    group_name="CoarseChunk",
    similarity="bm25_chinese", topk=3)

res = retriever("retrive")
print(res)