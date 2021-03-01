s1 = 'パトカーー'
s2 = 'タクシー'
string = ''

if len(s1) > len(s2):
    length = len(s2)
else:
    length = len(s1)

for i in range(length):
          string = string + s1[i] + s2[i]
        #string += (s1 + s2)[i::length] 意味不明
print(string)
