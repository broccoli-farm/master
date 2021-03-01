"""
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
"""
import random

def m(s):
    s = list(s) #random.shuffleを使うのにリストにした
    random.shuffle(s) #元のリストをランダムに並び変える関数
    return "".join(s) #17行目で文字列をつなげるためにした

def typoglycemia(s):
    if len(s) <= 4:
        return s
    else:
        return s[0] + m(s[1:-1]) + s[-1]

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
s = s.split()
s = [typoglycemia(i) for i in s]
print("".join(s))

"""
I cd o l u ' nt bl e e i ve that I co u ld at l u l a cy ue n n s d r t ad what I was re n d a ig : the pm o e a n h n el pw e or of the hu a mn mind .
"""
