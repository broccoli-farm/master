#記事中でカテゴリ名を宣言している行を抽出せよ．

import read20
import re

text = read20.file_reading()
text = text.split('\n')    #一行ごとに分けた

for line in text:
    if re.match(r'\[\[Category:.+\]\]', line):
        print(line)

"""
.
デフォルトのモードでは改行以外の任意の文字にマッチします
DOTALL フラグが指定されていれば改行も含む全ての文字にマッチします

+
直前の正規表現を 1 回以上繰り返したものにマッチさせる結果の正規表現にします
例えば ab+ は 'a' に 1 つ以上の 'b' が続いたものにマッチし、単なる 'a' にはマッチしません
"""
