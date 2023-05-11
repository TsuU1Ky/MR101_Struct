from TP6.projet.constantes import *
from view.Line import Line
from TP6.projet.types_labyrinthe import *
from view.Rectangle import Rectangle

def creerCellule() -> dict :
    cellule : dict = {const.NORD: None, const.SUD: None, const.EST: None,
                      const.OUEST: None, const.CONTENU: None}
    return cellule

def cellule_setMur(c: dict, dir: str, mur: Line) -> None :
    if not type_cellule(c):
        raise ValueError(f"Le paramètre {c} n’est pas une cellule.")
    if not type_direction(dir):
        raise ValueError(f"Le paramètre {c} n’est pas une direction.")
    if not type_mur(mur):
        raise ValueError(f"Le paramètre {c} n’est pas un mur.")

    c[dir] = mur

    return None

def cellule_getMur(c: dict, dir: str) -> Line :
    if not type_cellule(c):
        raise ValueError(f"Le paramètre {c} n’est pas une cellule.")
    if not type_direction(dir):
        raise ValueError(f"Le paramètre {c} n’est pas une direction.")

    mur : Line = c[dir]

    return mur

def cellule_setContenu(c: dict, content: Rectangle) -> None :
    if not type_cellule(c):
        raise ValueError(f"Le paramètre {c} n’est pas une cellule.")
    if not type_contenu(content):
        raise ValueError(f"Le paramètre {c} n’est pas un contenu.")

    c[const.CONTENU] = content

    return None

def cellule_getContenu(c: dict) -> Rectangle :
    if not type_cellule(c):
        raise ValueError(f"Le paramètre {c} n’est pas une cellule.")

    cont : Rectangle = c[const.CONTENU]

    return cont

def construireMur(hori:bool) -> Line :
    if hori:
        mur: Line = Line((0,0),(const.DIM_CELL,0))
        mur.setOutline(const.COLOR_MUR)
        mur.setWidth(3)
    else :
        mur: Line = Line((0, 0),(0, const.DIM_CELL))
        mur.setOutline(const.COLOR_MUR)
        mur.setWidth(3)

    return mur

def construireContenu() -> Rectangle :
    c : Rectangle = Rectangle((0, 0), (const.DIM_CELL, const.DIM_CELL))
    c.setFill(const.COLOR_FOND)
    c.noStroke()

    return c

