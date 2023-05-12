from TP6.projet.constantes import *
from TP6.projet.cellule import cellule_setCouleur
from view.Image import *
from random import randint
import const


def lc_to_px(lc: tuple) -> tuple:
    return (lc[1] + 1) * const.DIM_CELL, (lc[0] + 1) * const.DIM_CELL


def creerRobot(lab: list, pos: list, dir: str) -> dict:

    robot: dict = {
        const.IMAGE: Image(
            "mario.png", (lc_to_px(lab[0], lab[1])), (const.DIM_CELL, const.DIM_CELL)
        ),
        const.TRAJET: pos,
        const.COLOR_ROBOT: Color(randint(0, 255), randint(0, 255), randint(0, 255)),
        const.DIRECTION: dir,
    }

    return robot


def robot_getDirection(robot: dict) -> str:
    return robot[const.DIRECTION]


def robot_getPosition(robot: dict) -> tuple:
    return robot[const.TRAJET][-1]


def robot_getTrajet(robot: dict) -> list:
    return robot[const.TRAJET]


def robot_getColor(robot: dict) -> str:
    return robot[const.COLOR_ROBOT]


def deplacerRobot(labyrinthe: list, robot: dict, pos: tuple, dir: str) -> None:

    # Remplissage de la dernière case avec la couleur du robot
    cellule_setCouleur(
        labyrinthe[robot_getPosition(robot)],
        robot[const.COLOR_ROBOT],
    )

    # Mise à jour de la position de l'image du robot
    robot[const.IMAGE].position = lc_to_px(pos)

    # Mise à jour de la liste des positions du robot
    robot[const.TRAJET].append(pos)

    # Mise à jour de la direction du robot
    robot[const.DIRECTION] = dir

    return None


def getDirectionOpposee(direction: str) -> str:

    dir_oppo = None

    if direction == const.NORD:
        dir_oppo = const.SUD

    elif direction == const.SUD:
        dir_oppo = const.NORD

    elif direction == const.EST:
        dir_oppo = const.OUEST

    elif direction == const.OUEST:
        dir_oppo = const.EST

    return dir_oppo


def recolorerChemin(labyrinthe, dict_robots, numero):
    # Initialiser la couleur de remplissage à gris
    col = "gray"

    # Récupérer le robot correspondant à la clé numero
    robot = dict_robots[numero]

    # Récupérer la liste des déplacements du robot
    trajet = robot_getTrajet(robot)

    # Parcourir les cases du déplacement du robot en partant de la fin et tant que la couleur de la case du labyrinthe
    # correspond à celle du robot
    for i in range(len(trajet) - 1, -1, -1):
        pos = trajet[i]
        if labyrinthe[pos[0]][pos[1]] == robot_getColor(robot):
            # Si col vaut gray alors (on n’a pas trouvé de robot partageant le même chemin)
            if col == "gray":
                # Chercher dans la liste des robots, un robot différent de celui-ci et dont le chemin contient la
                # case en cours.
                for n, r in dict_robots.items():
                    if n != numero and pos in robot_getTrajet(r):
                        # Si un tel robot a été trouvé, affecter à col la couleur de ce robot.
                        col = robot_getColor(r)
                        break
            # Colorier la case avec la couleur col
            labyrinthe[pos[0]][pos[1]] = col
    return None


def trouverCheminLePlusCourt(labyrinthe: list, entree: tuple, sortie: tuple) -> list:
    # Initialisation de numero et du dictionnaire dict_robots
    numero = 1
    dict_robots = {}

    # Récupération de coord_entree et coord_sortie
    coord_entree = entree
    coord_sortie = sortie

    # Création du robot avec comme liste de positions une liste contenant un seul élément (les coordonnées de l'entrée)
    # et avec comme direction la valeur None
    robot = creerRobot(labyrinthe, [coord_entree], None)

    # Ajout du robot au dictionnaire dict_robots
    dict_robots[numero] = robot
    # Création du dictionnaire cases_vues avec le couple (coord_entree, numero)
    cases_vues = {coord_entree: numero}

    # Incrémentation de numero
    numero += 1

    # Initialisation du booléen fin à False
    fin = False

    # Début de la boucle tant que non fin
    while not fin:
        # Récupération des clés du dictionnaire dict_robots dans une liste
        keys = list(dict_robots.keys())

        # Pour toutes les clés k de cette liste
        for k in keys:
            # Récupération du robot correspondant à la clé k
            robot = dict_robots[k]

            # Copie/duplication de la liste des déplacements du robot dans dep_base
            dep_base = robot[const.TRAJET].copy()

            # Initialisation de n à 0
            n = 0

            # Enregistrement de l'opposé de la direction du robot dans dir_opp
            dir_opp = getDirectionOpposee(robot_getDirection(robot))

            # Pour toutes les directions dir possibles
            for direction, deplacement in [
                (const.NORD, (-1, 0)),
                (const.EST, (0, 1)),
                (const.SUD, (1, 0)),
                (const.OUEST, (0, -1)),
            ]:
                # Calcul de la nouvelle position p dans la direction dir
                p = (
                    robot_getPosition(robot)[0] + deplacement[0],
                    robot_getPosition(robot)[1] + deplacement[1],
                )

                # Si la case p n'a pas été visitée (si p ne fait pas partie des clés de cases_vues)
                # et la direction dir est différente de dir_opp (direction opposée du robot)
                if p not in cases_vues and direction != dir_opp:
                    # Incrémentation de n
                    n += 1

                    # Si n est égal à 1 (c'est le premier déplacement)
                    if n == 1:
                        # Déplacement du robot à la position p avec la direction dir
                        deplacerRobot(robot, p, direction)

                        # Enregistrement de (p, k) dans le dictionnaire cases_vues
                        cases_vues[p] = k
                    else:
                        # Duplication de la liste dep_base dans lst
                        lst = dep_base.copy()

                        # Création d'un nouveau robot avec la liste lst et la direction dir
                        new_robot = creerRobot(labyrinthe, lst, direction)

                        # Ajout du nouveau robot au dictionnaire dict_robots avec la clé numero
                        dict_robots[numero] = new_robot

                        # Ajout de (p, numero) dans le dictionnaire des cases visitées cases_vues
                        cases_vues[p] = numero

                        # Incrémentation de numero
                        numero += 1

                    # Si p vaut coord_sortie
                    if p == coord_sortie:
                        # Mettre fin à True
                        fin = True
                        # Récupérer le chemin le plus court qui correspond à celui du robot qui vient d'être déplacé ou créé
                        chemin = dict_robots[numero - 1][const.TRAJET]

                    # Si n vaut 0 (on n'a pas pu déplacer ce robot, il faut le supprimer)
                    if n == 0:
                        # Recolorier le chemin du robot qu'on va supprimer (voir ci-dessous)
                        recolorerChemin(
                            labyrinthe,
                            dict_robots[k][const.TRAJET],
                            const.COULEUR_CHEMIN,
                        )
                        # Supprimer la clé correspondante du robot du dictionnaire dict_robots
                        del dict_robots[k]
                # FinTantque

            # Récupérer le chemin le plus court qui correspond à celui du robot qui vient d'être déplacé ou créé
            chemin = dict_robots[numero - 1][const.TRAJET]

    return chemin
