# time:2023/3/23
import pandas as pd
from collections import Counter
from itertools import combinations
import numpy as np


def get_node_weight(path):
    df = pd.read_excel(path)
    counter = Counter()
    total = []
    for items in df.iloc[:, 0]:
        items = [item.strip(' ').lower().title() for item in items.split(';')]
        # print(items)
        if len(items) < 2:
            continue
        for item in combinations(items, 2):
            counter.update(['\t'.join(item)])

    for item in counter.most_common(3000):
    #for item in counter.items():
        print(item)
        source, target = item[0].split('\t')
        weight = item[1]
        temp = [source, target, weight]
        total.append(temp)
    print(total)
    total = pd.DataFrame(total, columns=['Source', 'Target', 'Weight'])
    # Weight 的计算方式
    #total['Weight'] = total[['Weight']].apply(lambda x: np.exp((x - np.min(x)+1) / (np.max(x) - np.min(x))))
    # total['Weight'] = total[['Weight']].apply(lambda x: (x - np.min(x) + 1))
    total.to_csv('../data/example.csv', index=False)
    print(counter.most_common(n=500))


if __name__ == '__main__':
    path = r'C:\Users\Administrator\PycharmProjects\python_gephi\Data Science-Machine Learning and Artificial Intelligence共现分析数据.xlsx'
    get_node_weight(path)
