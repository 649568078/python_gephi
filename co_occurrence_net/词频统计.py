import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'C:\Users\Administrator\PycharmProjects\python_gephi\Data Science, Machine Learning and Artificial Intelligence.xlsx')

# 将每一行按照';'分割成多个单词
words_list = df['Project Terms'].str.split(';')

# 将多个列表合并成一个列表
words = []
for row in words_list:
    if row == row:
        print(row)
        words += row

# 统计每个单词出现的频率
word_counts = pd.Series(words).value_counts()

print(word_counts)
word_counts.to_excel('word_counts.xlsx')