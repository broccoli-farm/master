"""
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json
import gzip

#gzip.open(filename, [mode], [compresslevel], [encoding], [errors], [newline])
def file_reading():
    with gzip.open('/Users/skr/Desktop/100/jawiki-country.json.gz','rt','utf-8') as f:
        for l in f:
            j = json.loads(l)
            if j["title"] == "イギリス":
                return j["text"]
    return "見つかりません．．．"


if __name__ == '__main__':
    print(file_reading())

"""
        for ["title"], ["text"] in j.items():
            if ["title"] == "イギリス":
                print(["text"])
"""
