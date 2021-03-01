"""
各行を3コラム目の数値の逆順で整列せよ
（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ
（この問題はコマンドで実行した時の結果と合わなくてもよい）．

日本語がまずわからん
"""
import sys
import pprint

#v = []
#k = []
d = {}

with open(sys.argv[1],'r') as f:
    for l in f:
        l = l.rstrip()
        #k.append(l)
        s = l.split('\t')
        thr = int(s[2])
        #v.append(thr)  #3行目抜きとったやつ
        d[l] = thr
#d = dict(zip(k, v))

d_sort = sorted(d.items(), key = lambda x: x[1], reverse=True)

pprint.pprint(d_sort)
