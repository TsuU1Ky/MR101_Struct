from TP6.projet.cellule import *
from TP6.projet.types_labyrinthe import *
from view.Canvas import Canvas
from random import *


def creerLabyrinthe(dim: tuple) -> list:
    if not type_dimension(dim):
        raise ValueError(f"Le paramètre {dim} n’est pas une dimension.")
    lab: list = []
    for i in range(dim[0]):
        col: list = []
        for j in range(dim[1]):
            col.append(creerCellule())
        lab.append(col)
    return lab


def labyrinthe_getCellule(labyrinthe: list, pos: tuple) -> dict:
    if not type_position(labyrinthe, pos):
        raise ValueError(f"{pos} n'est pas une position")

    return labyrinthe[pos[0]][pos[1]]


def formerLabyrinthe(cv: Canvas, labyrinthe: list) -> None:
    # Dessiner le fond du labyrinthe
    y = const.DIM_CELL
    for ligne in labyrinthe:
        x = const.DIM_CELL
        for cell in ligne:
            case: Rectangle = construireContenu()
            case.moveTo((x, y))
            cv.draw(case)
            cellule_setContenu(cell, case)
            x += const.DIM_CELL
        y += const.DIM_CELL

    # Dessiner les murs
    # Dessiner les murs Nord de la première ligne du labyrinthe
    x = const.DIM_CELL

    for cellule in labyrinthe[0]:

        mur = construireMur(hori=True)
        mur.moveTo((x, const.DIM_CELL))
        cv.draw(mur)
        cellule_setMur(cellule, const.NORD, mur)
        x += const.DIM_CELL

    # Dessiner les murs Est et Sud des cellules et par là même ceux de l’Ouest et du Nord des cellules voisines
    y = const.DIM_CELL

    for i in range(0, len(labyrinthe)):

        x = const.DIM_CELL
        mur = construireMur(hori=False)
        mur.moveTo((x, y))
        cv.draw(mur)
        cell = labyrinthe_getCellule(labyrinthe, (i, 0))
        cellule_setMur(cell, const.OUEST, mur)

        for j in range(0, len(labyrinthe[i])):

            mur = construireMur(hori=True)
            mur.moveTo((x, y + const.DIM_CELL))
            cv.draw(mur)
            cell = labyrinthe_getCellule(labyrinthe, (i, j))
            cellule_setMur(cell, const.SUD, mur)

            if i < len(labyrinthe) - 1:
                cell = labyrinthe_getCellule(labyrinthe, (i + 1, j))
                cellule_setMur(cell, const.NORD, mur)

            mur = construireMur(hori=False)
            mur.moveTo((x + const.DIM_CELL, y))
            cv.draw(mur)
            cell = labyrinthe_getCellule(labyrinthe, (i, j))
            cellule_setMur(cell, const.EST, mur)

            if i < len(labyrinthe[i]) - 1:
                cell = labyrinthe_getCellule(labyrinthe, (i, j))
                cellule_setMur(cell, const.OUEST, mur)

            x += const.DIM_CELL

        y += const.DIM_CELL

    return None


def labyrinthe_getNbLignes(labyrinthe: list) -> int:
    if not type_labyrinthe(labyrinthe):
        raise ValueError(f"{labyrinthe} n'est pas un labyrinthe")
    return len(labyrinthe)


def labyrinthe_getNbColonnes(labyrinthe: list) -> int:
    if not type_labyrinthe(labyrinthe):
        raise ValueError(f"{labyrinthe} n'est pas un labyrinthe")
    return len(labyrinthe[0])


def calculerNombreMurs(labyrinthe: list) -> int:
    if not type_labyrinthe(labyrinthe):
        raise ValueError(f"{labyrinthe} n'est pas un labyrinthe")

    nbl = labyrinthe_getNbLignes(labyrinthe)
    nbc = labyrinthe_getNbColonnes(labyrinthe)
    return (nbl - 1) * nbc + (nbc - 1) * nbl


def supprimerMurs(labyrinthe: list, pourcent: float) -> None:
    if not type_labyrinthe(labyrinthe):
        raise ValueError(f"{labyrinthe} n'est pas un labyrinthe")
    if not (0.0 < pourcent < 1.0):
        raise ValueError(
            f"Le pourcentage {pourcent} doit être compris entre 0.0 et 1.0 (exclu)"
        )

    ratio = pourcent * calculerNombreMurs(labyrinthe)
    i = 0

    while i < ratio:
        li = randint(0, labyrinthe_getNbLignes(labyrinthe) - 2)
        co = randint(0, labyrinthe_getNbColonnes(labyrinthe) - 2)
        cell = labyrinthe_getCellule(labyrinthe, (li, co))

        # Boucle pour récupérer les murs existant SUD ou EST dans la liste 'dir_murs'
        dir_murs = [
            dir for dir in [const.SUD, const.EST] if cell[dir] is not None
        ]

        if len(dir_murs) > 0:
            d = choice(dir_murs)
            cell[d].undraw()
            cell[d] = None

            if d == const.SUD and li + 1 < labyrinthe_getNbLignes(labyrinthe):
                cell_voisine = labyrinthe_getCellule(labyrinthe, (li + 1, co))
                # cell_voisine[const.NORD].undraw()
                cell_voisine[const.NORD] = None

            elif d == const.EST and co + 1 < labyrinthe_getNbColonnes(
                    labyrinthe):
                cell_voisine = labyrinthe_getCellule(labyrinthe, (li, co + 1))
                # cell_voisine[const.OUEST].undraw()
                cell_voisine[const.OUEST] = None

            i += 1

    return None


def colorier(labyrinthe: list, deb: tuple, color: Color) -> set:
    """
    Colorie une partie connexe du labyrinthe en partant de la cellule se trouvant en position deb selon l'algorithme de remplissage décrit ci-dessous et retourne l'ensemble des positions coloriées.

    :param labyrinthe: Labyrinthe à colorier
    :param deb: Position de départ de la cellule à colorier
    :param color: Couleur de remplissage
    :return: Ensemble des positions coloriées
    """

    if not type_labyrinthe(labyrinthe):
        raise ValueError(f"Le paramètre {labyrinthe} n'est pas un labyrinthe")

    positions_coloriées = set()
    positions_a_colorier = {deb}
    voisin_pos: tuple = (deb[0], deb[1])

    while len(positions_a_colorier) > 0:

        pos = positions_a_colorier.pop()
        cell = labyrinthe_getCellule(labyrinthe, pos)
        cellule_setCouleur(cell, color)
        positions_coloriées.add(pos)

        for dir in (const.NORD, const.SUD, const.EST, const.OUEST):
            if cellule_getMur(labyrinthe_getCellule(labyrinthe, pos),
                              dir) == None:

                # print(f"cell : {labyrinthe_getCellule(labyrinthe, pos)}\npos : {pos} dir :{dir}\n")

                if dir == const.NORD:
                    voisin_pos = pos[0] - 1, pos[1]

                elif dir == const.SUD:
                    voisin_pos = pos[0] + 1, pos[1]

                elif dir == const.EST:
                    voisin_pos = pos[0], pos[1] + 1

                elif dir == const.OUEST:
                    voisin_pos = pos[0], pos[1] - 1

            if (type_position(labyrinthe, voisin_pos)
                    and voisin_pos not in positions_coloriées):
                positions_a_colorier.add(voisin_pos)

    return positions_coloriées


def colorierTout(labyrinthe: list) -> list:
    if not type_labyrinthe(labyrinthe):
        raise ValueError(f"Le paramètre {labyrinthe} n'est pas un labyrinthe")

    positions_coloriées = set()
    res: list = []
    otp: list = []

    for i in range(len(labyrinthe)):

        for j in range(len(labyrinthe[i])):

            if (i, j) not in res:

                positions_coloriées = colorier(
                    labyrinthe,
                    (i, j),
                    Color(
                        randint(0, 255),
                        randint(0, 255),
                        randint(0, 255),
                    ),
                )
                res += positions_coloriées
                otp.append(positions_coloriées)

    return otp


def fusionnerCouleur(labyrinthe: list, s1: set, s2: set) -> None:

    if len(s1) > len(s2):
        cell = labyrinthe_getCellule(labyrinthe, list(s1)[0])
        col = cellule_getCouleur(cell)

        for elem in s2:
            cell = labyrinthe_getCellule(labyrinthe, elem)
            cellule_setCouleur(cell, col)

    else:
        cell = labyrinthe_getCellule(labyrinthe, list(s2)[0])
        col = cellule_getCouleur(cell)

        for elem in s1:
            cell = labyrinthe_getCellule(labyrinthe, elem)
            cellule_setCouleur(cell, col)

    return None


def fusionner(labyrinthe: list, lst: list) -> set:

    while len(lst) > 1:

        s = lst.pop()
        trouvé = False
        i = 0

        while not trouvé and i < len(lst):

            if getVoisinsEnsemble(s, lst[i]) != None:
                c1, c2 = getVoisinsEnsemble(s, lst[i])

                if type_position(labyrinthe, c1) and type_position(
                        labyrinthe, c2):
                    fusionnerCellules(labyrinthe, c1, c2)
                    fusionnerCouleur(labyrinthe, s, lst[i])
                    lst[i] = s | lst[i]
                    trouvé = True

            i += 1

        if not trouvé:
            raise ValueError(
                "Les ensembles ne forment pas une partition du labyrinthe")

    return lst[0]


def annulerColoriage(labyrinthe: list) -> None:

    for i in range(len(labyrinthe)):

        for j in range(len(labyrinthe[i])):

            cell = labyrinthe_getCellule(labyrinthe, (i, j))
            cellule_setCouleur(cell, const.COLOR_FOND)

    return None


def creerEntree(labyrinthe: list) -> None:

    cell = labyrinthe_getCellule(labyrinthe, (randint(0, 9), 0))
    cellule_setCouleur(cell, const.COLOR_ENTREE)

    return None


def creerSortie(labyrinthe: list) -> None:

    cell = labyrinthe_getCellule(labyrinthe,
                                 (randint(0, 9), len(labyrinthe[0]) - 1))
    cellule_setCouleur(cell, const.COLOR_SORTIE)

    return None


def getEntree(labyrinthe: list) -> tuple:

    for i in range(len(labyrinthe)):

        for j in range(len(labyrinthe[i])):

            if (labyrinthe_getCellule(labyrinthe,
                                      (i, j))[[const.CONTENU
                                               ]] == const.COLOR_ENTREE):
                return (i, j)

    return None


def getSortie(labyrinthe: list) -> tuple:

    for i in range(len(labyrinthe)):

        for j in range(len(labyrinthe[i])):

            if (labyrinthe_getCellule(labyrinthe,
                                      (i, j))[[const.CONTENU
                                               ]] == const.COLOR_SORTIE):
                return (i, j)

    return None


def getWin(lab: list) -> Canvas:
    return lab[0][0][const.CONTENU].canvas
