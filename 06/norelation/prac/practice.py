import nltk
import re
nltk.download('punkt')

NLP = "Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data."

#===== クリーニング =====
def clearn(text):
    text = re.sub(r',', '', text)
    text = re.sub(r'\.', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    return text

NLP = clearn(NLP)

#===== トークン化 =====
from nltk.tokenize import word_tokenize
NLP = word_tokenize(NLP)

#===== ストップワード =====
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = stopwords.words('english')
NLP = [word for word in NLP if word not in stop_words]

#=====　語幹の抽出 =====
from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()
NLP = [porter.stem(word) for word in NLP]
print(NLP)
