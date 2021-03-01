#記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

import read20
import re

text = read20.file_reading()
text = text.split('\n')
"""
for line in text:
    if re.match(r'^(={2,})\s*(.+)\s*', line):
        print(line)
"""
def section_level(line):
    section = re.sub(' ','',line)
    section = re.split('(={2,})|\s+', section)
    return section

for line in text:
    if re.match(r'^(={2,})\s*(.+?)\s*(={2,})$', line):
        #print(line)
        section = section_level(line)
        #print(section)
        level= len(section[1]) - 1
        #print(level)
        #if section[2] == '':
            #print('{section}:{level}'.format(section=section[4], level=level))
        #else:
        print('{section}:{level}'.format(section=section[2], level=level))

#+? 非貪欲 (non-greedy) あるいは 最小 (minimal) のマッチが行われ、できるだけ 少ない 文字にマッチします
