#テンプレートの内容を利用し，国旗画像のURLを取得せよ．

import dict28
import json
import urllib.request
import urllib.parse
import pprint

temp_dict = dict28.maru()
#print(temp_dict)
data = temp_dict["国旗画像"]
#print(data)

URL = 'https://en.wikipedia.org/w/api.php?'\
+ 'action=query'\
+ '&format=json'\
+ '&titles=File:' + urllib.parse.quote(data) \
+ '&prop=imageinfo'\
+ '&iiprop=url'

with urllib.request.urlopen(URL) as res:
    result = json.loads(res.read().decode())
    print(result['query']['pages']['-1']['imageinfo'][0]['url'])
#pprint.pprint(result)
"""
{'continue': {'continue': '||', 'iistart': '2011-10-03T04:05:02Z'},
 'query': {'pages': {'23473560': {'imageinfo': [{'descriptionshorturl': 'https://en.wikipedia.org/w/index.php?curid=23473560',
						 'descriptionurl': 'https://en.wikipedia.org/wiki/File:Flag_of_the_United_Kingdom.svg',
						 'url': 'https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg'}],
                                  'imagerepository': 'local',
                                  'ns': 6,
                                  'pageid': 23473560,
                                  'title': 'File:Flag of the United Kingdom.svg'}}}}
"""
