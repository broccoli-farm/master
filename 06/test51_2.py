import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


X_train = pd.read_table('./file/train.txt', header=None)
X_valid = pd.read_table('./file/valid.txt', header=None)
X_test = pd.read_table('./file//test.txt', header=None)
col = ['title', 'category']
X_train.columns = col
X_valid.columns = col
X_test.columns = col
X_train['dore'] = 'train'
X_valid['dore'] = 'valid'
X_test['dore'] = 'test'
col = ['title', 'category', 'dore']
#とりあえずデータ一回まとめてからしましょうね
data = pd.concat([X_train, X_valid, X_test]).reset_index(drop=True)
"""
あんまり理由はわかってないけど，Index値が重複している場合に
"Shape of passed values is (24044, 7), indices imply (16028, 7)"
ってエラーが出ちゃうらしくreset_indexとやらで前のインデックスを無効(drop=True)にして番号ふり直した
なんで？
#print(data.head(20))
"""
#CountVectorizerのコンストラクタにはtokenizer引数でわかち書き関数を渡します。
#tokenizerを指定しない場合のデフォルト設定ではスペースで文を単語に区切る処理が行われますが、これは英語のような単語をスペースで区切る言語を想定した動作です。
#tokenizerにcallable（関数、メソッドなど）を指定するとそれが文の分割に使われるので、日本語を対象にする場合は、自前で実装したわかち書き関数を指定するようにします。
vectorizer = CountVectorizer()
#　辞書
vectorizer.fit(data['category'])
# bow計算
bow = vectorizer.transform(data['category'])
data = pd.concat([data, pd.DataFrame(bow.toarray())], axis=1) #axit デフォルトは縦に結合させる toarray()でnumpy配列に変換

#もう一度queryで条件ごとに引っ張ってくることで振り分け直してからcolの列をdropで(列を指定するときはaxisは1行は0)で消して
X_train = data.query('dore=="train"').drop(col,axis=1)
X_valid = data.query('dore=="valid"').drop(col,axis=1)
X_test = data.query('dore=="test"').drop(col,axis=1)

X_train.to_csv('train.feature.txt', sep=' ', index=False, header=None)
X_valid.to_csv('valid.feature.txt', sep=' ', index=False, header=None)
X_test.to_csv('test.feature.txt', sep=' ', index=False, header=None)
