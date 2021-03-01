#単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""Wikiより　ジップの法則
出現頻度が k 番目に大きい要素が全体に占める割合が k分の1 に比例するという経験則である。
Zipf は「ジフ」と読まれることもある。また、この法則が機能する世界を「ジフ構造」と記する論者もいる。
包括的な理論的説明はまだ成功していないものの、様々な現象に適用できることが知られている。
この法則に従う確率分布（離散分布）をジップ分布という。
ジップ分布はゼータ分布（英語版）の特殊な形である。
"""
from scipy.stats import rankdata
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import nlp100_35
word_count = nlp100_35.count()


y = []
for key, value in word_count.items():
    y.append(value)

x = rankdata(-np.array(y))
x = x.astype(int)
y = np.log(y)

plt.scatter(x, y)
plt.xscale('log')
plt.yscale('log')

plt.savefig("/Users/skr/Desktop/100/result/filename39.png")
