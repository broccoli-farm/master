#25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

import re
import read20
#import pprint

text = read20.file_reading()
template_dictionary = {}

#25も関数にして持ってきた方がええんかな，わからんけど

basic_information = re.search(r'^\{\{基礎情報\s国\n(.*)\n\}\}$', text, re.MULTILINE + re.DOTALL)
basic_data = basic_information.group(1)
basic_data = re.split('\n(?=\|)', basic_data)

for line in basic_data:
    data = re.match(r'^\|(.+?)\s*\=\s*(.*)', line, re.DOTALL)  #???????????????
    if data == None:
        continue
    else:
        key = re.sub('\|','',data.group(1))
        key = re.sub('\s$','',key)
        value = re.sub('(\'{2,4})','',data.group(2))
        template_dictionary[key] = value
#pprint.pprint(template_dictionary, width=400)
for key, value in template_dictionary.items():
    print(key, value)
