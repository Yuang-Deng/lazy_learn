import lazyllm
from functools import partial

llm = lazyllm.OnlineChatModule(source='sensenova')
print(llm('你是谁'))

llm = lazyllm.TrainableModule(base_model = 'Qwen2-7B-Instruct', target_path = '/mnt/lustre/share_data/lazyllm/models/Qwen2-7B-Instruct')
llm.start()
print(llm('你是谁'))

def stream_call(m, query):
    with lazyllm.ThreadPoolExecutor(1) as executor:
        lazyllm.FileSystemQueue().dequeue()
        future = executor.submit(partial(m, llm_chat_history=[]), query)
        while True:
            if value := lazyllm.FileSystemQueue().dequeue():
                print(f'output: {""}'.join(value))
            elif future.done():
                break
        res = future.result()
        print(f'result: {res}')
        return res

m = lazyllm.TrainableModule(base_model = 'Qwen2-7B-Instruct', target_path = '/mnt/lustre/share_data/lazyllm/models/Qwen2-7B-Instruct').start()
r = m('你好,请帮我写⼀篇300字的作⽂,以知识库为题⽬')
m2 = m.share(prompt='请帮我对输⼊进⾏总结：')

m2(r)