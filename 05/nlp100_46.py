'''
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。」という例文を考える．
 この文は「作り出す」という１つの動詞を含み，「作り出す」に係る文節は「ジョン・マッカーシーは」，「会議で」，「用語を」であると解析された場合は，次のような出力になるはずである．

作り出す	で は を	会議で ジョンマッカーシーは 用語を
'''

import nlp100_41
data = nlp100_41.C_contact()
sources = dict()
for i in range(len(data)):
    for chunk in data[i]:
        for morph_d in chunk.morphs:
            if morph_d.pos == '動詞': #動詞が入っている文節かどうかが知りたい
                destination = morph_d.base  #動詞ならばmorphのベースを係り先の述語を入れておく変数に格納
                '''
                source_postpositional = []  #係り元の助詞のみのを入れておくリスト　これをキーにしたい
                source_phrase = []          #係り元の文節を入れておくリスト    こっちは値にする
                '''
                #sources.clear()
                for src in chunk.srcs:  #係り先の番号のリストを回す
                    for morph_s in data[i][src].morphs: #係り先のモルフ見るよ
                        if morph_s.pos == '助詞': #助詞の入っている文節ならば
                            phrase = ''.join([morph_s.surface if morph_s.pos != '記号' for morph_s in data[i][src].morphs])
                            #print(morph_s.surface)
                            #print(phrase)
                            sources[morph_s.surface] = phrase
                #ここから直す
                sources = sorted(sources.items()) #なんか中身がタプルになっちゃうから仕方なく
                #sources.clear()
                #sources.update(s)
                print(sources)
                """
                postpositional = ' '.join(sources.keys())
                phrase = ' '.join(sources.values())
                #postpositional = [num[0] for source in sources for num in source]
                if sources != '':
                    print('{}\t{}\t{}'.format(destination, postpositional, phrase))
                """
