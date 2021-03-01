#動詞の原形をすべて抽出せよ．

#表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）


import nlp100_30
neko_data = nlp100_30.reading_data()

for line in neko_data:
    for d in line:
        for k, v in d.items():
            if v == '動詞':
                print(d['base'])
