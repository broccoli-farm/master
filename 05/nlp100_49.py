"""
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を” -> “で連結して表現する
文節iとjに含まれる名詞句はそれぞれ，XとYに置換する

また，係り受けパスの形状は，以下の2通りが考えられる．

文節iから構文木の根に至る経路上に文節jが存在する場合:
文節iから文節jのパスを表示
上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を” | “で連結して表示

「ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。」という例文を考える． CaboChaを係り受け解析に用いた場合，次のような出力が得られると思われる．
Xは | Yに関する -> 最初の -> 会議で | 作り出した
Xは | Yの -> 会議で | 作り出した
Xは | Yで | 作り出した
Xは | Yという -> 用語を | 作り出した
Xは | Yを | 作り出した
Xに関する -> Yの
Xに関する -> 最初の -> Yで
Xに関する -> 最初の -> 会議で | Yという -> 用語を | 作り出した
Xに関する -> 最初の -> 会議で | Yを | 作り出した
Xの -> Yで
Xの -> 会議で | Yという -> 用語を | 作り出した
Xの -> 会議で | Yを | 作り出した
Xで | Yという -> 用語を | 作り出した
Xで | Yを | 作り出した
Xという -> Yを
"""

import nlp100_41
data = nlp100_41.C_contact()

def matte(x, y, sent):
    xs = []
    ys = []
    while x != y:
        if x < y:
            xs.append(x)
            x = sent[x].dst
        else:
            ys.append(y)
            y = sent[y].dst
    return xs, ys, x

def remove_noun(chunk): #名詞とかをとる用
    other = []
    for i, morph in enumerate(chunk.morphs):
        if morph.pos != '名詞' and morph.pos != '記号':
            other.append(morph.surface)#名詞か記号以外がきたらそこでループ終了でそこからの．．．
    return ''.join(other)   #要素の表層形をリストにぶちこんでいく

def assort(xs, ys, last, sent):
    xs = [sent[x] for x in xs]
    ys = [sent[y] for y in ys]
    last = sent[last]
    if xs and ys:   #文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合
        if len(xs) >= 2:
            xs = ['X' + remove_noun(xs[0])] + [' -> '.join(''.join([morph.surface for morph in x.morphs if morph.pos != '記号'])for x in xs[1:])]
        else:
            xs = ['X' + remove_noun(xs[0])]
        if len(ys) >= 2:
            ys = ['Y' + remove_noun(ys[0])] + [' -> '.join(''.join([morph.surface for morph in y.morphs if morph.pos != '記号'])for y in ys[1:])]
        else:
            ys = ['Y' + remove_noun(ys[0])]
        last = ''.join([morph.surface for morph in last.morphs if morph.pos != '記号'])
        return ' -> '.join(xs) + ' | ' + ' -> '.join(ys) + ' | ' + last
    else:   #文節iから構文木の根に至る経路上に文節jが存在する場合
        if len(xs) >= 2:
            xs = ['X' + remove_noun(xs[0])] + [' -> '.join(''.join([morph.surface for morph in x.morphs if morph.pos != '記号'])for x in xs[1:])]
        else:
            #xs = ['X' + remove_noun(xs[0])]
            xs = [''.join([morph.surface for morph in xs[0].morphs if morph.pos != '記号'])]
        #last = 'Y' + remove_noun(last)
        last = [''.join([morph.surface for morph in last.morphs if morph.pos != '記号'])]
        return ' -> '.join(xs + last)

#for i in range(len(data)):
for i in range(3):
    #名詞句を入れたリスト
    noun_first = [n for n in range(len(data[i])) if any(morph.pos == '名詞' for morph in data[i][n].morphs)]
    #print(noun_first)
    #名詞句と次に出てくる名詞句をセットにしたやつ
    pairs = [(noun_first[n], second) for n in range(len(noun_first)) for second in noun_first[n + 1:]]
    #print(pairs)
    for x, y in pairs:
        x_path, y_path, last = matte(x, y, data[i])
        #print(x_path,y_path,last)
        path = assort(x_path, y_path, last, data[i])
        print(path)
