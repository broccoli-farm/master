#動詞の表層形をすべて抽出せよ．

#得	動詞,自立,*,*,一段,未然形,得る,エ,エ
#0  0    1   2  3 4    5    6   7  8

import nlp100_30
neko_data = nlp100_30.reading_data()

for line in neko_data:
    for d in line:
        for k, v in d.items():
            if v == '動詞':
                print(d['surface'])
