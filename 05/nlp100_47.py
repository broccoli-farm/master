'''
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「また、自らの経験を元に学習を行う強化学習という手法もある。」という文から，以下の出力が得られるはずである．

学習を行う	に を	元に 経験を
'''

import nlp100_41
data = nlp100_41.C_contact()

sources = dict()

for i in range(len(data)):
    for chunk in data[i]:
        for morph_d in chunk.morphs:
            if morph_d.pos == '動詞': #動詞が入っている文節かどうかが知りたい
                #sources.clear()
                answer = ""
                for src in chunk.srcs:  #係り先の番号のリストを回す
                    for morph_s in data[i][src].morphs:
                        #if morph_s.pos == '記号':
                        if answer == "" and len(data[i][src].morphs)==2 and data[i][src].morphs[0].pos1 == 'サ変接続' and data[i][src].morphs[1].surface =='を':
                            answer = ''.join([data[i][src].morphs[0].surface, data[i][src].morphs[1].surface, morph_d.base])
                            break   #2個目はいらんからここで止める
                        elif morph_s.pos == '助詞': #助詞の入っている文節ならば
                            phrase = ''.join([morph_s.surface for morph_s in data[i][src].morphs if morph_s.pos != '記号'])
                            sources[morph_s.surface] = phrase
                #ここから直しましょう
                s = sorted(sources.items()) #なんか中身がタプルになっちゃうから仕方なく
                sources.clear()
                sources.update(s)
                postpositional = ' '.join(sources.keys())
                phrase = ' '.join(sources.values())
                if answer != "":
                    print('{}\t{}\t{}'.format("".join(answer), postpositional, phrase))
                break
