"""
各行の1列目の文字列の出現頻度を求め，
その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．

cut -f1 /Users/skr/Desktop/100/popular-names.txt | sort | uniq -c | sort -nr
"""
import sys

n = []
c = []
d = {}

with open(sys.argv[1],'r') as f:
    for line in f:
        line = line.split("\t")
        n.append(line[0])   #各行の一列目のみ取り出す
        c.append(0)

s = set(n)
d.update(zip(s, c))
#print(d)

for key,value in d.items(): #各要素のキーkeyと値valueの両方に対してforループ処理を行いたい場合は、items()メソッドを使う
    for l in n:
        if l == key:
            value = value + 1
            d[key] = value

for key, value in sorted(d.items(), key = lambda x: x[1], reverse=True):
    print(str(value) + " " + str(key))

"""
valueで並び替える場合は，ラムダ式(その場に関数定義を記述する方法)やユーザー定義関数を使用してソート条件を指定する．
降順の場合は，reverseオプションを使う．
ans = sorted(d.items(), key=lambda x:x[1], reverse=True)
key=lambda x: x[1]がなかったらキーのアルファベット順になった
                ↑を0にしたら上と同じ
#lambda式の形式
lambda 引数:処理内容
"""
