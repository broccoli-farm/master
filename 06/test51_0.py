import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('stopwords')

def clearn(text):
    #文字を消す
    text = re.sub(r'\W', ' ', text)
    return text

def count(datas):
    word_count = {}
    for sentences in datas:
        for sentence in sentences:
            if sentence[1] == 'JJ' or sentence[1] == 'JJR' or sentence[1] == 'JJS' or sentence[1] == 'NN' or sentence[1] == 'NNS' or sentence[1] == 'NNP' or sentence[1] == 'NNPS' or sentence[1] == 'RB' or sentence[1] == 'RBR' or sentence[1] == 'RBS' or sentence[1] == 'VB' or sentence[1] == 'VBD' or sentence[1] == 'VBG' or sentence[1] == 'VBN' or sentence[1] == 'VBP' or sentence[1] == 'VBZ':
                word = sentence[0]
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

#(b = business, t = science and technology, e = entertainment, m = health)
infile = ['test.txt','train.txt','valid.txt']
#outfile = ['test.feature.txt','train.feature.txt','valid.feature.txt']
#for input, output in zip(infile, outfile):
#for input in infile:
    #with open(input, 'r') as inf:
with open('test.txt', 'r') as inf, open('business.txt', 'w') as outf1, open('science_and_technology.txt', 'w') as outf2, open('entertainment.txt', 'w') as outf3, open('health.txt', 'w') as outf4:
    datas = []
    #category = {}
    for line in inf:
        data = line.split('\t')
        #print(data)
        datas.append(data)
        #category.update(data[0])
    categories = ['b','t','e','m']
    #for ctg in category:
        #ctg = []    #これでいいのか
    b = []
    t = []
    e = []
    m = []
    sentence = []
    for data in datas:
        datafirst = clearn(data[1])
        datafirst = word_tokenize(datafirst)    #トークン化
        stop_words = stopwords.words('english') #ストップワード 今回は使わない
        datafirst = [word for word in datafirst if word not in stop_words]  #ここ多分英語での終わりの記号っていうか目印があったらそこで終了みたいになってんのかなあとで見よ？あ違うかも
        porter = PorterStemmer()    #語幹抽出
        answer1 = [porter.stem(word) for word in datafirst]
        #print(answer1)
        answer2 = nltk.pos_tag(datafirst) #品詞を見てる
        onlypos = [pos for part, pos in answer2]    #品詞だけのリストをつくる
        #print(onlypos)
        for (genkei, pos) in zip(answer1, onlypos):
            sentence.append([genkei, pos])
            #print([genkei, pos])
        if data[0] == "b":    #もっときれいにかけそうやけど思いつかん　関数にしたらいいんかな
            b.append(sentence)
        elif data[0] == "t":
            t.append(sentence)
        elif data[0] == "e":
            e.append(sentence)
        elif data[0] == "m":
            m.append(sentence)
        #print(sentence)
        sentence = []
    b_count = count(b)
    t_count = count(t)
    e_count = count(e)
    m_count = count(m)
    for key, value in sorted(b_count.items(), key = lambda x: x[1], reverse=True):
        outf1.write(str(value) + " " + str(key) + '\n')
        #print(str(value) + " " + str(key))
    for key, value in sorted(t_count.items(), key = lambda x: x[1], reverse=True):
        outf2.write(str(value) + " " + str(key) + '\n')
    for key, value in sorted(e_count.items(), key = lambda x: x[1], reverse=True):
        outf3.write(str(value) + " " + str(key) + '\n')
    for key, value in sorted(m_count.items(), key = lambda x: x[1], reverse=True):
        outf4.write(str(value) + " " + str(key) + '\n')
"""
JJ	Adjective
JJR	Adjective, comparative
JJS	Adjective, superlative

NN Noun, singular or mass
NNS Noun, plural
NNP Proper noun, singular
NNPS Proper noun, plural

RB	Adverb
RBR	Adverb, comparative
RBS	Adverb, superlative

VB	Verb, base form
VBD	Verb, past tense
VBG	Verb, gerund or present participle
VBN	Verb, past participle
VBP	Verb, non-3rd person singular present
VBZ	Verb, 3rd person singular present
"""
