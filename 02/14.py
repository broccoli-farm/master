"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
"""
#head -n 5 /Users/skr/Desktop/100/popular-names.txt

import sys

t = []
a = int(sys.argv[2])

with open(sys.argv[1],'r') as f:
    for line in f:
        line = line.rstrip()
        t.append(line)

for i in range(len(t)):
    if i <= (a - 1):
        print("".join(t[i]))
