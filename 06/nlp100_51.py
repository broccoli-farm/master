"""
学習データ，検証データ，評価データから特徴量を抽出し，それぞれtrain.feature.txt，valid.feature.txt，test.feature.txtというファイル名で保存せよ．
なお，カテゴリ分類に有用そうな特徴量は各自で自由に設計せよ．
記事の見出しを単語列に変換したものが最低限のベースラインとなるであろう．
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import feature51
#X_train = pd.read_table('./file/train.txt', header=None)
X_valid = pd.read_table('valid.txt', header=None)
#X_test = pd.read_table('./file//test.txt', header=None)
col = ['title', 'category']
#X_train.columns = col
X_valid.columns = col
#X_test.columns = col
#X_train['dore'] = 'train'
X_valid['dore'] = 'valid'
#X_test['dore'] = 'test'
col = ['title', 'category', 'dore']
#とりあえずデータ一回まとめてからしましょうね
#data = pd.concat([X_train, X_valid, X_test]).reset_index(drop=True)
#結局使うん
#tfidf_vectorizer = TfidfVectorizer(use_idf=True,lowercase=False)
#category = [i for i in data['category']]
#tf_idf = feature51.vectorizer_transform(data['category'])
tf_idf = feature51.vectorizer_transform(X_valid['category'])
#print(tf_idf)
#pd.concatでdataに上で出したものをくっつける
data = pd.concat([X_valid, pd.DataFrame(tf_idf.toarray())], axis=1)
#axit デフォルトは縦に結合させる toarray()でnumpy配列に変換

#もう一度queryで条件ごとに引っ張ってくることで振り分け直してからcolの列をdropで(列を指定するときはaxisは1行は0)で消して
#X_train = data.query('dore=="train"').drop(col,axis=1)
X_valid = data.query('dore=="valid"').drop(col,axis=1)
#X_test = data.query('dore=="test"').drop(col,axis=1)

#X_train.to_csv('train.feature.txt', sep=' ', index=False, header=None)
X_valid.to_csv('valid.feature.txt', sep=' ', index=False, header=None)
#X_test.to_csv('test.feature.txt', sep=' ', index=False, header=None)
