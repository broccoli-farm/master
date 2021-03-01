"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，
"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""
def n_gram(s, n):
    return [s[i:i+n] for i in range(len(s) -n +1)]

if __name__ == '__main__':
    s = "I am an NLPer"
    splited = s.split()
    print('単語bi-gram =',n_gram(s,2))
    print('文字bi-gram =',n_gram(splited,2))
else:
    print(__name__)
