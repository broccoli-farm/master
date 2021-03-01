"""
単語の出現頻度のヒストグラムを描け．
ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
"""

import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import nlp100_35
word_count = nlp100_35.count()

x = []
for key, value in word_count.items():
    x.append(value)

x = np.array(x)

#print(max(x))  9194　最大値
#print(len(x))  11235　単語の異なり

plt.hist(x, bins = 10, range = (1, max(x)))
#bins：棒の数,range：ビンの最小値から最大値→横軸？
plt.savefig("/Users/skr/Desktop/100/result/filename38.png")
#問題文の解釈が間違ってるのかそれっぽくないヒストグラムしか表示されん
