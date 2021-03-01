"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
"""
#tail -n 5

import sys

t = []
a = int(sys.argv[2])

with open(sys.argv[1],'r') as f:
    for line in f:
        line = line.rstrip()
        t.append(line)

n = len(t)
for i in range(n):
    if i >= (n - a):    #末尾のn行を出力
        print("".join(t[i]))
