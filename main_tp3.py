# main_tp3.py
from TP3.tp3 import indexOf


def test_indexOf() -> None :
 lst = [ 4, 2, 8, 5, 6, 5, 3, 1 ]
 print(f"Recherche de 5 dans {lst} : index = {indexOf(lst, 5)}")
 print(f"Recherche de 9 dans {lst} : index = {indexOf(lst, 9)}")
 return None
test_indexOf()

from TP3.tp3 import indexOfSorted
...
def test_indexOfSorted() -> None :
 lst = [4, 2, 8, 5, 6, 5, 4, 1]
 lst.sort()
 print(f"Recherche de 5 dans {lst} : index, nombre itérations = {indexOfSorted(lst, 5)}")
 print(f"Recherche de 3 dans {lst} : index, nombre itérations = {indexOfSorted(lst, 3)}")
 return None
test_indexOfSorted()

from TP3.tp3 import binarySearch
...
def test_binarySearch() -> None :
 lst = [4, 2, 8, 5, 6, 5, 4, 1]
 lst.sort()
 print(f"Recherche de 5 dans {lst} : index, nombre itérations = {binarySearch(lst, 5)}")
 print(f"Recherche de 3 dans {lst} : index, nombre itérations = {binarySearch(lst, 3)}")
 return None
test_binarySearch()

from TP3.tp3 import devinerNombre
#devinerNombre(1, 20)

def test_getIndexOfRect(fn : callable) ->None :
 from TP1.tp1 import getRandomList
 from TP3.tp3_complementaire import createCanvas, createRectList,getIndexOfSortedRect
 from random import randint
 from view.Canvas import waitClick
 from view.Chrono import Chrono

 chrono = Chrono()

 lst = getRandomList(80, 0, 400)
 lst.sort()
 cv= createCanvas(lst)
 rectlst= createRectList(cv, lst)
 nb = randint(0, 400)
 chrono.start()
 idx= fn(lst, nb)
 chrono.stop()
 timezz = chrono.getTime()
 print(f"Valeur recherchée : {nb} n\ Index de la valeur : {idx} n\ Temps écoulé : {timezz} n\ Cliquez sur la fenêtre pour finir ...")
 waitClick()

from TP3.tp3_complementaire import getIndexOfSortedRect
test_getIndexOfRect(getIndexOfSortedRect)
