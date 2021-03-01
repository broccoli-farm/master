"""
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""

def temp(x, y, z):
    return '{h}時の{kion}は{temp}'.format(h =x,kion =y, temp=z)

x = 12
y = "気温"
z = 22.4

print(temp(x, y, z))
