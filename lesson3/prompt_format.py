import lazyllm

def prompter(p, query):
    m = lazyllm.TrainableModule('internlm2-chat-7b').prompt(p('你好，我是LazyLLM开发的人工智能助手，{input}'))
    print(m(query))

query = '你好'
print('=' * 30)
prompter(lazyllm.AlpacaPrompter, query)
print('-' * 30)
prompter(lazyllm.ChatPrompter, query)
print('=' * 30)