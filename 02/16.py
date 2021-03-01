"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
"""

#split -l 278 /Users/skr/Desktop/100/popular-names.txt /Users/skr/Desktop/100/sp16.txt

"""
split [-a sufflen(サフィックス長)] [-b byte_count(バイト数［k｜m)] [-l line_count] [-p pattern] [file [prefix]]
"""

import sys

n = input("何分割したいですか")
n = int(n)
hako = []
count = 0
j = 0

with open("/Users/skr/Desktop/100/popular-names.txt","r") as f:
    for l in f:
        #l = l.rstrip()
        hako.append(l)
        count = count + 1

num = count/n
amari = count%n

for i in range(0,len(hako),n):
    #h = hako[i:n+i]
    fname = '/Users/skr/Desktop/100/file16no' + str(j) + '.txt'
    with open(fname, 'w') as f:
        f.write("".join(hako[i:n+i]))
    j = j + 1

"""メモ）556だと5個ファイルできta確認しやすい
for i in range(0,len(hako),n):  #n回ずつ回す
    #p_new = pathlib.Path    #空ファイルを作成したいパス
    with open('/Users/skr/Desktop/100/sub16.txt', mode='w') as f:
        f.write("".join(hako[i:n+i])) #iからn個の値とっってくる

    #print(hako[i:n+i])
"""
"""もう無理や
with open('/Users/skr/Desktop/100/sub16.txt', mode='w') as f:
    f.write("\n".join(kara))
    f.write("\n")

    if i <= c:
        print(hako[i])
    else:
        print("\n")
        c = c + n
"""
