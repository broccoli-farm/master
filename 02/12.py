#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．

"""
cut -f1 /Users/skr/Desktop/100/popular-names.txt > /Users/skr/Desktop/100/col1.txt
cut -f2 /Users/skr/Desktop/100/popular-names.txt > /Users/skr/Desktop/100/col2.txt
&&つかってつないだら一回でいける
"""

col1 = []
col2 = []

with open("/Users/skr/Desktop/100/popular-names.txt","r") as f, open('/Users/skr/Desktop/100/col1.txt', mode='w') as f1, open('/Users/skr/Desktop/100/col2.txt', mode='w') as f2:
    for i in f:
        l = i.split()  #１列目を分解する
        f1.write("\n".join(l[0]))   #１列目の０個目の要素（1列目）をcol1にいれる
        f2.write("\n".join(l[1]))   #１列目の０個目の要素（2列目）をcol2にいれる
"""
with open('/Users/skr/Desktop/100/col1.txt', mode='w') as f:
    f.write("\n".join(col1))
with open('/Users/skr/Desktop/100/col2.txt', mode='w') as f:
    f.write("\n".join(col2))
"""
#うまくいったのでは
