import lazyllm
# ⽂档加载
documents = lazyllm.Document(dataset_path="data_kb")
# 检索组件定义
retriever = lazyllm.Retriever(doc=documents, group_name="CoarseChunk", similarity="bm25_chinese", topk=3, output_format='content', join='')
retriever.start()
# ⽣成组件定义
prompt = ('You will act as an AI question-answering assistant and complete a dialogue task.'
'In this task, you need to provide your answers based on the given context and questions.')
llm = lazyllm.OnlineChatModule(source='sensenova').prompt(lazyllm.ChatPrompter(instruction=prompt, extro_keys=['context_str']))
# 推理, 将query和召回节点中的内容组成dict，作为⼤模型的输⼊
query = '介绍一下马库斯'
res = llm({"query": query, "context_str": retriever(query=query)})
print(f'With RAG Answer: {res}')