#タブ1文字につきスペース1文字に置換せよ．

"""
awk '{gsub("\t", " ", $0); print $0}' popular-names.txt
perl -pe 's/\t/ /g' popular-names.txt
sed 's/\t/ /g'  popular-names.txt
expand -t 1 popular-names.txt
sedはStream EDitor の略 多機能なコマンドらしい

tr '\t' ' ' < /Users/skr/Desktop/100/popular-names.txt
．
"""
import sys
#a=[]
with open(sys.argv[1],'r') as fa , open(sys.argv[2],'w') as fb:
    for line in fa:
        line = line.rstrip().replace("\t", " ")
        #a.append(line)
        fb.write(line)

#with open(sys.argv[2],'w') as f:
    #f.write("\n".join(line))
"""
num = len(line)
#print(num)
for i in range(num):
    l = line
#print(l)
"""
