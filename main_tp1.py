# main_tp1.py

from TP1.tp1 import getRandomList
from TP1.tp1 import compter

for i in range(5):
    print(getRandomList(10, -5, 5))

print("\n") #saut de ligne pour séparer les fonctions

test_liste=getRandomList(10, -5, 5)
for _ in range(5):
    print(test_liste)
    print("Nombre de 0 : ", compter(test_liste, 0))
    print("Nombre de 10 : ", compter(test_liste, 10))
