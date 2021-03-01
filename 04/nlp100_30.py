import MeCab
"""
#def nekosama():
with open('/Users/skr/Desktop/100/neko.txt') as input,open('/Users/skr/Desktop/100/neko.txt.mecab', mode='w') as output:
    mecab = MeCab.Tagger()
    output.write(mecab.parse(input.read()))
"""

'''
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''
#得	動詞,自立,*,*,一段,未然形,得る,エ,エ
#0  0    1   2  3 4    5    6   7  8

#import pandas as pd
import re
#filename = "/Users/skr/Desktop/100/neko.txt.mecab"
"""
df = pd.read_table('/Users/skr/Desktop/100/neko.txt.mecab',  engine='python', sep='\t|,', header=None, usecols=[0, 1, 2, 7], names=['surface', 'pos', 'pos1', 'base'])
print(df)
"""
def reading_data():
    with open('/Users/skr/Desktop/100/neko.txt.mecab','r') as f:
        #\n\nになってるんか知らんけど変に区切られる
        #text_data = f.read()#.split("\n")
        text_data = re.split(r"(?<=[^\t\n])\n", f.read())
        #text_data = re.sub(r'\n\t', '\\', text_data)
        answer = []
        sentence = []
        #print(text_data)
        for line in text_data:
            if line == "EOS":
                answer.append(sentence)
                sentence = []
            elif re.match(r'.*\t',line, re.DOTALL):
                d = {}
                data = re.split(r"\t",line)
                #print(data[1])
                if data[0] == '\n':
                    continue
                else:
                    s = data[1].split(',')
                    d = {'surface':data[0], 'base':s[6], 'pos':s[0], 'pos1':s[1]}
                    sentence.append(d)
            else:
                continue
        """
        ans =[]
        for num in answer:  #空のリストを消す
            if not num:
                continue
            else:
                ans.append(answer)
        """
    return answer
#print(ans)
if __name__ == '__main__':
    data = reading_data()
    for num in data:
        for line in num:
            print(line)
