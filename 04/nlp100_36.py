#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

#なんかよくわからんけどいっぱいインポートしてる（よくわからんことはない）
import numpy as np
#pip install japanize-matplotlib
import matplotlib.pyplot as plt
import japanize_matplotlib    #豆腐文字っていうのになったから仕方なく
import re
from collections import defaultdict
import nlp100_30
neko_data = nlp100_30.reading_data()

word_count = defaultdict(int)
for data in neko_data:
    for line in data:
        if line['pos'] == "記号":  #記号を含まないように
            continue
        else:
            word = line['base']
            word_count[word] += 1
#print(word_count)
left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
label = []
height = []
for key, value in sorted(word_count.items(), key = lambda x: x[1], reverse=True):
    label.append(key)
    height.append(value)

left = np.array(left)
height = np.array(height[:10])

print(label[:10], height)

plt.bar(left, height, tick_label=label[:10], align="center")
#plt.show()
plt.savefig("/Users/skr/Desktop/100/result/filename36.png")
