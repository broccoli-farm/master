#26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ

import re
import read20
#import pprint

text = read20.file_reading()
template_dictionary = {}

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
        if re.search(r'\[\[.+\]\]', value):
            value = re.sub('[\[\]#\|]','',value)
        template_dictionary[key] = value
#pprint.pprint(template_dictionary, width=400)
for key, value in template_dictionary.items():
    print(key, value)
