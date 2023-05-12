from TP6.projet.labyrinthe import *
from TP6.projet.labyrinthe import *
from view.Canvas import Canvas, waitClick
from view.Color import black, gray
from TP6.projet.constantes import const

nb_lignes = 10
nb_colonnes = 30

lab = creerLabyrinthe((nb_lignes, nb_colonnes))

win: Canvas = Canvas(
    ((nb_colonnes + 2) * const.DIM_CELL, (nb_lignes + 2) * const.DIM_CELL)
)
win.drawFrame(gray)


formerLabyrinthe(win, lab)
supprimerMurs(lab, 0.5)

lst = colorierTout(lab)
fusionnerCellules(lab, (9, 28), (9, 27))
print(f"(9, 29) : {labyrinthe_getCellule(lab, (9, 29))}")
print(f"(9, 28) : {labyrinthe_getCellule(lab, (9, 28))}")
print(f"(9, 27) : {labyrinthe_getCellule(lab, (9, 27))}")
s = fusionner(lab, lst)
annulerColoriage(lab)

creerEntree(lab)
creerSortie(lab)

waitClick()
