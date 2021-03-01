'''
与えられた文の係り受け木を有向グラフとして可視化せよ
'''

from graphviz import Digraph
import nlp100_41
data = nlp100_41.C_contact();

relations = []
for chunk in data[2]:   #2個目の文章で　
  if int(chunk.dst) != -1:
    source = ''.join([morph.surface if morph.pos != '記号' for morph in chunk.morphs])
    destination = ''.join([morph.surface if morph.pos != '記号' for morph in data[2][int(chunk.dst)].morphs])
    relation = [source, destination]
    relations.append(relation)

rel_gra = Digraph(format='png') #画像はデフォルトではpdfで保存される
rel_gra.attr('node', shape='circle')
for sour, dest in relations:
    rel_gra.edge(sour, dest)
rel_gra.render("tree")
rel_gra.view()
