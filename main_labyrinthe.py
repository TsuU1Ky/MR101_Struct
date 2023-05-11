from TP6.projet.labyrinthe import *
from view.Canvas import Canvas, waitClick
from view.Color import black
from TP6.projet.constantes import const

nb_lignes = 10
nb_colonnes = 30

lab = creerLabyrinthe((nb_lignes,nb_colonnes))

win : Canvas = Canvas(((nb_colonnes + 2) * const.DIM_CELL, (nb_lignes + 2)*const.DIM_CELL))
win.drawFrame(black)

formerLabyrinthe(win,lab)
waitClick()