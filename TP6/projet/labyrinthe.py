from TP6.projet.cellule import *
from TP6.projet.types_labyrinthe import *
from view.Canvas import Canvas

def creerLabyrinthe(dim:tuple) -> list :
    if not type_dimension(dim):
        raise ValueError(f"Le paramètre {dim} n’est pas une dimension.")
    lab: list = []
    for i in range(dim[0]):
        col: list = []
        for j in range(dim[1]):
            col.append(creerCellule())
        lab.append(col)
    return lab

def labyrinthe_getCellule(labyrinthe:list, pos:tuple) -> dict :
    if not type_position(labyrinthe, pos):
        raise ValueError(f"{pos} n'est pas une position")

    return labyrinthe[pos[0]][pos[1]]

def formerLabyrinthe(cv:Canvas, labyrinthe:list) -> None:
    # Dessiner le fond du labyrinthe
    y = const.DIM_CELL
    for ligne in labyrinthe:
        x = const.DIM_CELL
        for cell in ligne:
            case : Rectangle = construireContenu()
            case.moveTo((x,y))
            cv.draw(case)
            cellule_setContenu(cell,case)
            x += const.DIM_CELL
        y += const.DIM_CELL

    # Dessiner les murs
    # Dessiner les murs Nord de la première ligne du labyrinthe
    x = const.DIM_CELL

    for cellule in labyrinthe[0] :

        mur = construireMur(True)
        mur.moveTo((x,const.DIM_CELL))
        cv.draw(mur)
        cellule_setMur(cellule,"Nord",mur)
        x += const.DIM_CELL

    # Dessiner les murs Est et Sud des cellules et par là même ceux de l’Ouest et du Nord des cellules voisines
    y = const.DIM_CELL

    for i in range (0,len(labyrinthe)):

        x = const.DIM_CELL
        mur = construireMur(False)
        mur.moveTo((x,y))
        cv.draw(mur)
        cell = labyrinthe_getCellule(labyrinthe, (i, 0))
        cellule_setMur(cell,"Ouest",mur)

        for j in range(0, len(labyrinthe[i])):

            mur = construireMur(True)
            mur.moveTo((x, y+const.DIM_CELL))
            cv.draw(mur)
            cell = labyrinthe_getCellule(labyrinthe, (i, j))
            cellule_setMur(cell, "Sud", mur)

            if i < len(labyrinthe)-1 :
                cell = labyrinthe_getCellule(labyrinthe, (i+1, j))
                cellule_setMur(cell, "Nord", mur)

            mur = construireMur(False)
            mur.moveTo((x+const.DIM_CELL, y))
            cv.draw(mur)
            cellule_setMur(cell, "Est", mur)

            if i < len(labyrinthe[i])-1 :
                cell = labyrinthe_getCellule(labyrinthe, (i, j))
                cellule_setMur(cell, "Ouest", mur)

            x += const.DIM_CELL

        y += const.DIM_CELL
    return None





