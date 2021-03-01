"""
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を” -> “で連結する
「ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。」という例文を考える． CaboChaを係り受け解析に用いた場合，次のような出力が得られると思われる．

ジョンマッカーシーは -> 作り出した
AIに関する -> 最初の -> 会議で -> 作り出した
最初の -> 会議で -> 作り出した
会議で -> 作り出した
人工知能という -> 用語を -> 作り出した
用語を -> 作り出した
"""

import nlp100_41
data = nlp100_41.C_contact()

for i in range(len(data)):
    for chunk in data[i]:
        for morph in chunk.morphs:
            if morph.pos == '名詞':
                noun_phrase = [''.join([mor.surface for mor in chunk.morphs if mor.pos != '記号'])]
                while chunk.dst != -1:  # 名詞があるchunkのdstを見て行ってリストにいれていく
                    noun_phrase.append(''.join(mor.surface for mor in data[i][chunk.dst].morphs if mor.pos != '記号'))
                    chunk = data[i][chunk.dst]
                if len(noun_phrase) >= 2:
                    print(' -> '.join(noun_phrase))
