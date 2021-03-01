#行数をカウントせよ．確認にはwcコマンドを用いよ．

"""
wc -l /Users/skr/Desktop/100/popular-names.txt
wcコマンド(word count)
"""
import sys

print(sys.argv[0])
#s=[]
count = 0
with open(sys.argv[1],'r') as f:
    for line in f:
        #s.append(line.replace("\t", " "))
        count = count + 1
print(count)

"""
# ファイルをひらく
a_file = open("/Users/skr/Desktop/100/100-2/popular-names.txt")
#テキストを読む
s = a_file.read()
# ファイルを閉じる
a_file.close()

print(s)

num =len(s)

print(num)
"""
"""
# 一行ずつ読み込んで表示する
for line in a_file:
  print (line)
"""
