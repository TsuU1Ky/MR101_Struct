# projet/types_labyrinthe.py

from TP6.projet.constantes import *
from view.Line import Line
from view.Rectangle import Rectangle


def type_direction(d: object) -> bool:
    """
    Détermine si le paramètre correspond bien à une direction parmi const.NORD, const.SUD, const.EST et const.OUEST

    :param d: objet à tester
    :return: `True` si l'objet correspond à une direction, `False` sinon.
    """
    return d in [const.NORD, const.SUD, const.EST, const.OUEST]


def type_mur(m: object) -> bool:
    """
    Détermine si l'objet passé en paramètre peut correspondre à un mur ou non.
    Prend en compte l'implémentation en mode texte.

    :param m: Objet à tester
    :return: `True` si l'objet peut correspondre à un mur, `False` sinon
    """
    return m is None or type(m) == Line or type(m) == bool


def type_contenu(c: object) -> bool:
    """
    Détermine si l'objet passé en paramètre peut correspondre à un contenu de cellule ou non.
    Prend en compte l'implémentation en mode texte.

    :param c: Objet à tester
    :return: `True` si l'objet peut correspondre à un contenu, `False` sinon
    """
    return c is None or type(c) == Rectangle or type(c) == str


def type_cellule(cell: object) -> bool:
    """
    Vérifie que le paramètre correspond bien à une cellule.
    Prend en compte l'implémentation en mode texte.

    :param cell: objet à vérifier
    :return: `True` si le paramètre est une cellule, `False` sinon.
    """
    res = True
    if cell is not None:
        if type(cell) != dict: # Ce n'est pas un dictionnaire, donc ce n'est pas une cellule
            res = False
        else:
            # Vérification des clés du dictionnaire
            for c in [const.NORD, const.SUD, const.EST, const.OUEST, const.CONTENU]:
                if c not in cell:
                    res = False # Il manque une clé/propriété dans le dictionnaire
            if res:
                # Vérification des types des propriétés
                # Vérification des types des murs
                for c in [const.NORD, const.SUD, const.EST, const.OUEST]:
                    if not type_mur(cell[c]):
                        res = False # Le type des murs ne correspond pas
                # Vérification du type du contenu
                if res and not type_contenu(cell[const.CONTENU]):
                    res = False # Le type du contenu ne correspond pa
    return res


def type_dimension(d: object) -> bool:
    """
    Détermine si l'objet passé en paramètre peut correspondre à une dimension (w, h) ou non.

    :param d: Objet à tester
    :return: `True` si l'objet peut correspondre à une dimension, `False` sinon.
    """
    return type(d) == tuple and len(d) == 2 and d[0] > 0 and d[1] > 0


def type_labyrinthe(lab: object) -> bool:
    """
    Détermine si l'objet passé en paramètre peut correspondre ou non à un labyrinthe.

    :param lab: objet à tester
    :return: `True` si l'objet peut correspondre à un labyrinthe, `False` sinon.
    """
    res = True
    # Un labyrinthe doit être une liste
    if type(lab) != list:
        res = False
    else:
        i = 0
        while i < len(lab) and res:
            # Chaque élément de la liste doit être une liste (tableau 2D : liste de listes)
            if type(lab[i]) != list:
                res = False
            else:
                j = 0
                # Chaque élément du tableau 2D doit être une cellule
                while j < len(lab[i]) and res:
                    if not type_cellule(lab[i][j]):
                        res = False
                    j += 1
            i += 1
    return res


def type_position(lab: list, pos: tuple) -> bool:
    """
    Vérifie que le premier paramètre est bien un labyrinthe et que le second représente bien
    une position dans le labyrinthe.

    :param lab: Labyrinthe
    :param pos: Position dans ce labyrinthe
    :return: `True` si les deux paramètres sont corrects, `False` sinon.
    """
    res = True
    if not type_labyrinthe(lab):
        res = False
    elif not(0 <= pos[0] < len(lab)) or not(0 <= pos[1] < len(lab[pos[0]])):
        res = False
    return res
