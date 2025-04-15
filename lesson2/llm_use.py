import lazyllm

llm_prompt = "你是⼀只⼩猫，每次回答完问题都要加上喵喵喵"
llm = lazyllm.OnlineChatModule(source="sensenova",
model="DeepSeek-R1").prompt(llm_prompt)
lazyllm.WebModule(llm, port=23466, history=[llm]).start().wait()