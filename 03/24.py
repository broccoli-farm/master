#記事から参照されているメディアファイルをすべて抜き出せ．

import read20
import re

text = read20.file_reading()

fileline = re.findall(r'(?<=ファイル:)[^\|\]]+', text)
for line in fileline:
    print(line)

"""
def mediafile(line):
    data = re.search(r'(?<=ファイル:)[^\|\]]+', line)
    return data.group()

for line in text:
    if re.search(r'ファイル:', line):
        #print(line)
        print(mediafile(line))
"""
#[^ ]括弧内に含まれない１文字
