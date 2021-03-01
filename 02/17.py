"""
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはcut, sort, uniqコマンドを用いよ．

skr@WadaSakuranoAir ~ % cut -f1 /Users/skr/Desktop/100/popular-names.txt | sort | uniq
"""

import sys

n = []

with open(sys.argv[1],'r') as f:
    for line in f:
        line = line.split("\t")
        n.append(line[0])   #各行の一列目のみ取り出す

n = set(n)  #重複を消す
s = sorted(n)   #あいうえお順にするまちがえたアルファベット順

print("\n".join(s))
"""

with open(sys.argv[1],'r') as f:
    names = {line.split('\t')[0] for line in f}
#print('\n'.join(names))
print(names)
"""
