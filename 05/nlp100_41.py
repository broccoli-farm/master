"""
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），
          係り先文節インデックス番号（dst），
          係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストの係り受け解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
冒頭の説明文の文節の文字列と係り先を表示せよ．本章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

# * 0 17D 1/1 0.388993
from collections import defaultdict
import sys

class Morph:
    #表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
    def __init__(self, surface, base, pos, pos1):
        #初期化
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def __str__(self):
        return 'surface[{0}]\tbase[{1}]\tpos[{2}]\tpos1[{3}]'.format(self.surface, self.base, self.pos, self.pos1)

class Chunk:
    #形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst）， 係り元文節インデックス番号のリスト（srcs）
    def __init__(self ,morphs ,dst ,srcs):
        #self.chunk_id = chunk_id
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
    def __str__(self):
        return 'morphs[{0}], dst[{1}], srcs{2}'.format(', '.join([morph.surface for morph in self.morphs]), self.dst, self.srcs)

def C_contact():
    sentence = []
    sentences = []
    morphs = []
    srcs = defaultdict(list)
    filename = '/Users/skr/Desktop/100/ai.ja.txt.parsed'
    with open(filename, 'r') as f:
    #with open(sys.argv[1], 'r') as f:
        for line in f:
            member = line.split()   #member[0]:文節番号, member[1]:係り先インデックス番号
            if line[0] == '*':
                if member[1] != '0':    #0がきたら文節がかわります
                    sentence.append(Chunk(morphs, dst, srcs[num]))
                    morphs = []
                num = int(member[1])
                dst = int(member[2].rstrip('D'))
                if dst != -1:
                    srcs[dst].append(num)
            elif line != 'EOS\n':
                ot = member[1].strip().split(',')  #baseに「\n*」って確か出てきてしまったから消すためにストリップ使用
                morphs.append(Morph(member[0], ot[6], ot[0], ot[1]))
            else:
                sentence.append(Chunk(morphs, dst, srcs[num]))
                morphs = []
                srcs.clear()
                sentences.append(sentence)
                #morphs = []
                sentence = []

    return sentences

if __name__ == '__main__':
    result = C_contact()
    for i in range(3):
        for num in result[i]:
            print(num)
