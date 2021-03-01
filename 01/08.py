"""
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
 英小文字ならば(219 - 文字コード)の文字に置換
 その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

#ord()関数で英小文字をUnicodeコードポイントに変換
#chr()関数に219-(取得した数値)で暗号処理を行う。

def cipher(text):
    ans = ""
    for i in text:
        if i.islower(): #すべての文字が小文字かどうか判定 ※文字列型じゃ無いと無理？
            ans += chr(219 - ord(i))
        else:
            ans += i
    return ans

t = input("暗号化，複合化をします．文字列を入れてね")

a = cipher(t)
print("暗号化　" + a)

f = cipher(a)
print("復号化　" + f)

"""
文字列apple
暗号化　zkkov
復号化　apple

暗号化，複合化をします．文字列を入れてねI am Sakura
暗号化　I zn Szpfiz
復号化　I am Sakura
"""
