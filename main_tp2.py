# main_tp2.py
from TP1.tp1 import getRandomList
from TP2.tp2 import triBullesRect
from TP2.tp2 import triSelectionRect
from TP2.tp2 import triInsertionRect
from TP2.tp2 import estTrie
from TP2.tp2 import quickSort
from TP2.tp2 import quickSortRect
from random import randint

from view.Canvas import Canvas
from view.Canvas import Canvas, waitClick
from view.Rect import Rect, getCanvasSizeFrom
from view.Rectangle import Rectangle
from view.Color import Color
from view.Chrono import Chrono

chrono = Chrono()
nb: int = 20
tps: float = 0.01
lst = getRandomList(nb, 20, 300)
rectlst = []

cv: Canvas = Canvas(getCanvasSizeFrom(lst))


for w in range(len(lst)):
    rectlst.append(Rect(w, lst[w], cv))

print("Lancement du tri : cliquez dans la fenêtre")
waitClick()
chrono.start()
triSelectionRect(rectlst, tps)
chrono.stop()
triSelecTime = chrono.getTime()
print("Fin du tri : cliquez pour finir")
waitClick()

for r in rectlst:
    r.undraw()
rectlst=[]
waitClick()
for w in range(len(lst)):
    rectlst.append(Rect(w, lst[w], cv))

print("Lancement du tri : cliquez dans la fenêtre")
waitClick()
chrono.start()
triBullesRect(rectlst, tps)
chrono.stop()
triBulleTime = chrono.getTime()
print("Fin du tri : cliquez pour finir")
waitClick()

for r in rectlst:
    r.undraw()
rectlst=[]
for w in range(len(lst)):
    rectlst.append(Rect(w, lst[w], cv))

print("Lancement du tri : cliquez dans la fenêtre")
waitClick()
chrono.start()
triInsertionRect(rectlst, tps)
chrono.stop()
triInsertTime = chrono.getTime()
print("Fin du tri : cliquez pour finir")
waitClick()

for r in rectlst:
    r.undraw()
rectlst=[]
for w in range(len(lst)):
    rectlst.append(Rect(w, lst[w], cv))

print("Lancement du tri : cliquez dans la fenêtre")
waitClick()
chrono.start()
quickSortRect(rectlst, tps)
chrono.stop()
triQSTime = chrono.getTime()
print("Fin du tri : cliquez pour finir")
waitClick()

print(f"Temps pour le trie de selection : {triSelecTime}, Temps pour le trie à bulles : {triBulleTime},"
      f" Temps pour le trie d'insertion : {triInsertTime}, Temps pour le trie quickSort : {triQSTime}")
