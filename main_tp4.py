#imports
from random import randint
from TP4.tp4 import getRegularArray2D, getMin, getMax, isRegular, getSize2D, getCarre2D, getSommeLignes, getSommeColonnes, getSommeDiagonale1, \
    getSommeDiagonale2, zeros, creerCarremagique, getNbParLigne, getArray2D, copyArray2D, transforme2D1D, transforme1D2D

def test_getRegularArray2D() -> None :

 lst = getRegularArray2D(4, 5, -10, 10)
 print("Tableau de 4 lignes et 5 colonnes :", lst, sep="\n")

 return None

#test_getRegularArray2D()


def test_getMinMax() -> None:
    for _ in range (5):
        lst = getRegularArray2D(randint(1,5), randint(1,5), -10, 10)
        mn =getMin(lst)
        mx = getMax(lst)
        print(f"{lst}\nMin = {mn}\nMax ={mx}\n")

    return None

#test_getMinMax()

def test_getRegularArray2D() -> None :
    nl = randint(1,10)
    nc = randint(1,10)
    tab = getRegularArray2D(nl, nc, randint(-20,-5), randint(5,20))
    i = 0

    while i < 10000 :

        nl = randint(1,10)
        nc = randint(1,10)
        tab = getRegularArray2D(nl, nc, randint(-20,-5), randint(5,20))

        i += 1

    assert isRegular(tab) and (getSize2D(tab) == (nl,nc)) and (getMin(tab) < getMax(tab)), "Une erreur s'est produite !"
    print("La fonction getRegularArray2D est correcte !")
    return None

#test_getRegularArray2D()

def test_getCarre2D () -> None :
    for _ in range (5):
        nb = randint(3,6)
        print(getCarre2D(nb))
    return None

#test_getCarre2D()

def test_getSommeLignes() -> None :
    for _ in range (4):
        tab = getCarre2D(3)
        print(tab, ", somme des lignes : ", getSommeLignes(tab))
    return None

#test_getSommeLignes()

def test_getSommeColonnes() -> None :
    for _ in range (4):
        tab = getCarre2D(3)
        print(tab, ", somme des colonnes : ", getSommeColonnes(tab))
    return None

#test_getSommeColonnes()

def test_getSommeDiagonale1() -> None :
    for _ in range (4):
        tab = getCarre2D(3)
        print(tab, ", somme de la diagonale principale : ", getSommeDiagonale1(tab))
    return None

#test_getSommeDiagonale1()

def test_getSommeDiagonale2() -> None :
    for _ in range (4):
        tab = getCarre2D(3)
        print(tab, ", somme de la diagonale secondaire : ", getSommeDiagonale2(tab))
    return None

#test_getSommeDiagonale2()

def test_dessinerCarre() -> None :


def test_zeros() -> None :
    m = zeros(4, 7)
    print(m)
    m[0][2] = 10
    print(m)
    return None

#test_zeros

def test_creerCarreMagique() -> None :
    tab = creerCarremagique(3)
    print(tab)

#test_creerCarreMagique()

def test_remplir2D() -> None :
    from TP1.tp1 import getRandomList
    from TP4.tp4 import getArray2D, remplir2D

    lst = getRandomList(7, 0, 10)
    tab = getArray2D(lst)
    print(tab)
    remplir2D(tab, -10, 10)
    print(tab)

    return None

#test_remplir2D()

def test_copy() -> None :
    arr = getArray2D([3, 2, 1])
    print("arr =", arr)
    arr2 = copyArray2D(arr)
    arr[0][2] = 10
    arr[1][1] = 20
    arr[2][0] = 30
    print("arr =", arr)
    print("arr2 =", arr2)
    return None

#test_copy()

def test_transforme2D1D()-> None:
    tab= [[ 2, 3, 1 ], [ 6, 4 ], [ 9, 0, 5 ]]
    print(transforme2D1D(tab))
    return None

#test_transforme2D1D()

def test_transforme1D2D() -> None :
    print(transforme1D2D(lst, -1))
    return None

#test_transforme1D2D()