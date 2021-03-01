"""
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
import nlp100_05

s1 = "paraparaparadise"
s2 = "paragraph"

X = ngram5.n_gram(s1,2)
Y = ngram5.n_gram(s2,2)

print(s1,'の文字bi-gram =',X)
print(s2,'の文字bi-gram =',Y)

#set()関数を使って、リストをset（集合）に変換
X = set(X)
Y = set(Y)

print('XとYの和集合 =',X|Y)
print('XとYの積集合 =',X&Y)
print('XからYの差集合 =',X-Y)
print('YからXの差集合 =',Y-X)

print('’se’というbi-gramがXに含まれているか','se' in X)
print('’se’というbi-gramがYに含まれているか','se' in Y)

"""
|　:　和集合
-　:　差集合
&　:　積集合
^　:　対称差集合
"""
