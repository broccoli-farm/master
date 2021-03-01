'''
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''

import nlp100_41
data = nlp100_41.C_contact();

for i in range(3):
    for chunk in data[i]:
      if int(chunk.dst) != -1:
          for morph_sou, morph_dst in zip(chunk.morphs, data[i][int(chunk.dst)].morphs):
            if morph_sou.pos == '名詞' and morph_dst.pos == '動詞':
                source = ''.join([morph.surface if morph.pos != '記号' for morph in chunk.morphs])
                destination = ''.join([morph.surface if morph.pos != '記号' for morph in data[i][int(chunk.dst)].morphs])
                print(source, destination, sep='\t')
