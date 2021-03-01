#記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

#カテゴリの名前だけ？とってくるの？

import read20
import re

text = read20.file_reading()
text = text.split('\n')    #一行ごとに分けた
"""
def CategoryName(line):
    name = re.match(r'\[\[Category:(.*)\]\]', line)
    name_group = name.group(1).split('|')
    return name_group[0]
"""
def category_name(line):
    name = re.search(r'(?<=Category:)\w+', line)
    return name.group()

for line in text:
    if re.match(r'\[\[Category:.+\]\]', line):
        print(category_name(line))
#[ぁ-んァ-ン一-龥0-9０−９a-zA-Z・] = \w
