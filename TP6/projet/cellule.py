from TP6.projet.constantes import *
from view.Line import Line
from view.Color import Color
from TP6.projet.types_labyrinthe import *
from view.Rectangle import Rectangle
from view.Canvas import Canvas, waitClick
import time


def creerCellule() -> dict:
    cellule: dict = {
        const.NORD: None,
        const.SUD: None,
        const.EST: None,
        const.OUEST: None,
        const.CONTENU: None,
    }
    return cellule


def cellule_setMur(c: dict, dir: str, mur: Line) -> None:
    if not type_cellule(c):
        raise ValueError(f"Le paramètre {c} n’est pas une cellule.")
    if not type_direction(dir):
        raise ValueError(f"Le paramètre {dir} n’est pas une direction.")
    if not type_mur(mur):
        raise ValueError(f"Le paramètre {mur} n’est pas un mur.")

    c[dir] = mur

    return None


def cellule_getMur(c: dict, dir: str) -> Line:
    if not type_cellule(c):
        raise ValueError(f"Le paramètre {c} n’est pas une cellule.")
    if not type_direction(dir):
        raise ValueError(f"Le paramètre {dir} n’est pas une direction.")

    mur: Line = c[dir]

    return mur


def cellule_setContenu(c: dict, content: Rectangle) -> None:
    if not type_cellule(c):
        raise ValueError(f"Le paramètre {c} n’est pas une cellule.")
    if not type_contenu(content):
        raise ValueError(f"Le paramètre {content} n’est pas un contenu.")

    c[const.CONTENU] = content

    return None


def cellule_getContenu(c: dict) -> Rectangle:
    if not type_cellule(c):
        raise ValueError(f"Le paramètre {c} n’est pas une cellule.")

    cont: Rectangle = c[const.CONTENU]

    return cont


def construireMur(hori: bool) -> Line:
    if hori:
        mur: Line = Line((0, 0), (const.DIM_CELL, 0))
        mur.setOutline(const.COLOR_MUR)
        mur.setWidth(3)
    else:
        mur: Line = Line((0, 0), (0, const.DIM_CELL))
        mur.setOutline(const.COLOR_MUR)
        mur.setWidth(3)

    return mur


def construireContenu() -> Rectangle:
    c: Rectangle = Rectangle((0, 0), (const.DIM_CELL, const.DIM_CELL))
    c.setFill(const.COLOR_FOND)
    c.noStroke()

    return c


def cellule_setCouleur(c: dict, color: Color) -> None:
    c[const.CONTENU].setFill(color)
    return None


def cellule_getCouleur(c: dict) -> Color:
    return c[const.CONTENU].getFill()


def estVoisin(c1: tuple, c2: tuple) -> bool:
    res = False

    if ((c2[0] == c1[0] - 1 or c2[0] == c1[0] + 1) and c2[1] == c1[1]) or (
        (c2[1] == c1[1] - 1 or c2[1] == c1[1] + 1) and c2[0] == c1[0]
    ):
        res = True
    return res


def getCelluleVoisine(cell: tuple, s: set) -> tuple:

    voisin = None
    i = 0

    while i < len(s) and voisin == None:

        if estVoisin(cell, list(s)[i]):

            voisin = list(s)[i]

        i += 1

    return voisin


def getVoisinsEnsemble(s1: set, s2: set) -> tuple:

    voisins = None
    i = 0

    while i < len(s1) and voisins == None:

        j = 0

        while j < len(s2):

            if estVoisin(list(s1)[i], list(s2)[j]):

                voisins: tuple = (list(s1)[i], list(s2)[j])
            j += 1
        i += 1
    return voisins


def fusionnerCellules(labyrinthe: list, c1: tuple, c2: tuple) -> None:

    cell1 = labyrinthe[c1[0]][c1[1]]
    cell2 = labyrinthe[c2[0]][c2[1]]

    if c1[0] - 1 == c2[0]:
        print(f"Supp mur NORD Cellule1 : {c1}\nSupp mur SUD Cellule2 : {c2}\n")

        cell1[const.NORD].undraw()
        cell2[const.SUD].undraw()
        cell1[const.NORD] = None
        cell2[const.SUD] = None

    elif c1[0] + 1 == c2[0]:
        print(f"Supp mur SUD Cellule1 : {c1}\nSupp mur NORD Cellule2 : {c2}\n")

        cell1[const.SUD].undraw()
        cell2[const.NORD].undraw()
        cell1[const.SUD] = None
        cell2[const.NORD] = None

    elif c1[1] - 1 == c2[1]:
        print(f"Supp mur OUEST Cellule1 : {c1}\nSupp mur EST Cellule2 : {c2}\n")

        cell1[const.OUEST].undraw()
        cell2[const.EST].undraw()
        cell1[const.OUEST] = None
        cell2[const.EST] = None

    elif c1[1] + 1 == c2[1]:
        print(f"Supp mur EST Cellule1 : {c1}\nSupp mur OUEST Cellule2 : {c2}\n")

        cell1[const.EST].undraw()
        cell2[const.OUEST].undraw()
        cell1[const.EST] = None
        cell2[const.OUEST] = None

    return None
