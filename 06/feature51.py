from math import log
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from scipy.sparse import csr_matrix

def tf(t, d):
    #各文章内での単語の出現頻度. たくさん出現する単語ほど重要.
    return d.count(t) / len(d)

def df(t, docs):
    #ある単語が出現する文章の数.
    df = 0
    for doc in docs:
        df += 1 if t in doc else 0
    return df

def idf(t, docs):
    #それぞれの単語がいくつの文書内で共通して使われているか.
    #単語がレアであるほど高い値を指す
    N = len(docs)
    return log(N/df(t, docs))+ 1

def clearn(s):
    #記号とかを消す
    s = re.sub(r'\W', ' ', s)
    s = s.lower()
    return s

def vectorizer_transform(text):
    # 単語を生成
    words = []
    newtexts = []
    for s in text:
        data = clearn(s)
        #print(data)
        data = word_tokenize(data)#トークン化
        stop_words = stopwords.words('english')#ストップワード 計算に含めない単語?
        data = [word for word in data if word not in stop_words]
        porter = PorterStemmer()    #語幹抽出
        s = [porter.stem(word) for word in data]
        newtexts.append(' '.join(s))
        words += s#.split(' ')
    words = list(set(words))
    words.sort()
    tf_idf = []
    for txt in newtexts:
        line_tf_idf = []
        for w in words:
            # tfを計算
            tf_v = tf(w, txt)

            # idfを計算
            idf_v = idf(w, newtexts)

            # tfとidfを乗算
            line_tf_idf.append(tf_v * idf_v)
        tf_idf.append(line_tf_idf)
    tf_idf = csr_matrix(tf_idf)
    return tf_idf

if __name__ == '__main__':
    # ベクトル化する文字列
    text = [
       'Apple computer of the apple mark',
       'linux computer is unix like',
       'windows computer'
    ]

    tf_idf = vectorizer_transform(text)

    for line in tf_idf:
        print(line)
