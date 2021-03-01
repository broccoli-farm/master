#27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

import re
import read20
#import pprint

def maru():
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
                value = re.sub('[\[\]#\|]','', value)
            if re.search(r'\{\{.+\}\}', value):
                value = re.sub('[{}]','', value)
            pattern = re.compile(r'\[http:([^]]*)\]')
            value = pattern.sub(r'', value)
            template_dictionary[key] = value
    return template_dictionary

if __name__ == '__main__':
    #pprint.pprint(maru(), width=400)
    dictionary = maru()
    for key, value in dictionary.items():
        print(key, value)
