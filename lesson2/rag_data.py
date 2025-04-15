import os
from datasets import load_dataset
dataset = load_dataset('cmrc2018')
# 基于测试集中的context字段创建⼀个知识库，每10条数据为⼀个txt，最后不⾜10条的也为⼀个txt
context = list(set([i['context'] for i in dataset['test']])) # 去重后获得256个语料
# 计算需要的⽂件数
chunk_size = 10
total_files = (len(context) + chunk_size - 1) // chunk_size # 向上取整
# 创建⽂件夹data_kb保存知识库语料
os.makedirs("data_kb", exist_ok=True)
# 按 10 条数据⼀组写⼊多个⽂件
for i in range(total_files):
    chunk = context[i * chunk_size : (i + 1) * chunk_size] # 获取当前 10 条数据
    file_name = f"./data_kb/part_{i+1}.txt" # ⽣成⽂件名
with open(file_name, "w", encoding="utf-8") as f:
    f.write("\n".join(chunk))