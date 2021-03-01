'''
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をメンバ変数に持つこととする．
さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，
各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．
'''


class Morph:
    #表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.surface, self.base, self.pos, self.pos1)

sentences = []
morphs = []
filename = '/Users/skr/Desktop/100/ai.ja.txt.parsed'
with open(filename, 'r') as f:
    for line in f:
        if line[0] == '*':
            continue
        elif line != 'EOS\n':
            surface = line.split('\t')
            #ot = surface[1].strip().split(',')  #baseに「\n*」って確か出てきてしまったから消すためにストリップ使用
            ot = surface[1].rstrip().split(',')
            morphs.append(Morph(surface[0], ot[6], ot[0], ot[1]))
        else:
            sentences.append(morphs)
            morphs = []
"""全部
for i in range(0, len(sentences)):
    for num in sentences[i]:
        print(vars(num))
    #print(num.__dict__)
"""
#冒頭の説明文はリストsentenceの３個目の要素（2番目は空）
#for i in range(3):
for num in sentences[2]:
    print(num)
