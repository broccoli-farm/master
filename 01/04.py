"""

1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への
連想配列（辞書型もしくはマップ型）を作成せよ．
"""

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
#length = len(s)
splited = s.split()
#print(splited[0])
el = {}

for i, s in enumerate(splited): #enunmerate()で番号，要素をえた
    if i+1 in num:  #先頭の1文字
        el[i+1] = s[0]  #s番目の要素の０番目の文字をelのi+1番目にいれるよ
    else:
        el[i+1] = s[:2]  #2文字
print(el)

#j = input("元素記号を入力してね")
"""
ss = []
#print(ss[0])

i = 0
for i in range(length):
    if i+1 in num:
        ss = splited[i]
        el.insert(i,ss[0])
    else:
        ss = splited[i]
        el.insert(i,ss[0:2])
print(el)
"""

"""
splited_in = [s for s in splited if num in s]
print(splited_in)
"""
