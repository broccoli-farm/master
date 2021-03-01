"""
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""

#paste col1.txt col2.txt

import sys
"""
with open("/Users/skr/Desktop/100/col1.txt","r") as f1:
    first = f1.readlines()
with open("/Users/skr/Desktop/100/col2.txt","r") as f2:
    second = f2.readlines()
"""
#re
with open ("/Users/skr/Desktop/100/col1.txt","r") as f1, open("/Users/skr/Desktop/100/col2.txt","r") as f2, open('/Users/skr/Desktop/100/merge.txt', mode='w') as f:
    for l1,l2 in zip(f1,f2):
        f.write(l1.rstrip() +  "\t" + l2)
#before
    """
    def merge(first,second):
        first = first.rstrip()  #改行文字を消したかった
        second = second.rstrip()    #こっちは一応しといただけ
        #rstrip() で引数を省略すると末尾のあらゆる改行文字と空白文字を除去できる
        #for i in range(len(first)):
        return first + "\t" + second
    """
    """
        res = [merge(i,j) for i,j in zip(first,second)]
        f.write("\n".join(res))
    """
#print('\n'.join(res))
"""
with open('/Users/skr/Desktop/100/merge.txt', mode='w') as f:
    f.write("\n".join(res))
"""
"""
え，できたやん．
"""
