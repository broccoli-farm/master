"""
学習データ（train.txt），検証データ（valid.txt），評価データ（test.txt）を作成せよ．

ダウンロードしたzipファイルを解凍し，readme.txtの説明を読む．
情報源（publisher）が”Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com”, “Daily Mail”の事例（記事）のみを抽出する．
抽出された事例をランダムに並び替える．
抽出された事例の80%を学習データ，残りの10%ずつを検証データと評価データに分割し，それぞれtrain.txt，valid.txt，test.txtというファイル名で保存する．
ファイルには，１行に１事例を書き出すこととし，カテゴリ名と記事見出しのタブ区切り形式とせよ（このファイルは後に問題70で再利用する）．
学習データと評価データを作成したら，各カテゴリの事例数を確認せよ．
"""
import random
datas = []
with open('/Users/skr/Desktop/100/06/NewsAggregatorDataset/newsCorpora.csv', 'r') as f:
    for line in f:
        data = line.replace('"', '\'')
        data = data.split('\t')
        if data[3] == 'Reuters' or data[3] == 'Huffington Post' or data[3] == 'Businessweek' or data[3] == 'Contactmusic.com' or data[3] == 'Daily Mail':
            datas.append(data)
            #print(data[3])

random.shuffle(datas)
train = int(len(datas)*0.8)
#この処理をした方がいいのかせんでもいいのか考えるんが面倒やからとりあえずした方が確実やししておく
if int(len(datas)-train//2) == 0:
    valid=test= int((len(datas)-train)/2)
else:   #もし余が出たら（出るか？）残りの一件をtrainに入れる
    valid=test= int((len(datas)-train)/2)
    train = train + 1

with open('/Users/skr/Desktop/100/06/train.txt', 'w') as f1, open('/Users/skr/Desktop/100/06/valid.txt', 'w') as f2, open('/Users/skr/Desktop/100/06/test.txt', 'w') as f3:
    for data in datas[:train]:  #trainまで
        f1.write('\t'.join([data[4], data[1]])+'\n')
    for data in datas[train:train+valid]:   #train~train+valid
        f2.write('\t'.join([data[4], data[1]])+'\n')
    for data in datas[train+valid:]:    #あまり
        f3.write('\t'.join([data[4], data[1]])+'\n')


"""
test.txt : 570 156 513 97 = 1336
train.txt : 4495 1192 4280 717 = 10684
valid.txt : 562 177 501 96 = 1336
"""
