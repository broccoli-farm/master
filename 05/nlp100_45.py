'''
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
ただし，出力は以下の仕様を満たすようにせよ．

 動詞を含む文節において，最左の動詞の基本形を述語とする
 述語に係る助詞を格とする
 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。」という例文を考える．
この文は「作り出す」という１つの動詞を含み，「作り出す」に係る文節は「ジョン・マッカーシーは」，「会議で」，「用語を」であると解析された場合は，次のような出力になるはずである．

作り出す	で は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「行う」「なる」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
'''

import nlp100_41
data = nlp100_41.C_contact()

for i in range(len(data)):
    for chunk in data[i]:
      for morph_d in chunk.morphs:
        if morph_d.pos == '動詞':
            destination = morph_d.base
            for src in chunk.srcs:
                source = [morph_s.surface for morph_s in data[i][src].morphs if morph_s.pos == '助詞']
            source.sort()
            source = ' '.join(source)
            if source != '':
                print('{}\t{}'.format(destination, source))
