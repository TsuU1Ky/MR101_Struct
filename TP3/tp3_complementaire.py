from view.Canvas import Canvas
from view.Rect import Rect, getCanvasSizeFrom, setPlaced

def getIndexOfRect (lst:list, val:int) -> int:
        ind = -1
        i = 0
        nbElem = len(lst)

        while ind == -1 and i < nbElem:
            if lst[i].getHeight() == val:
                ind = i
            i += 1

        return ind

def createCanvas (lst:list) -> Canvas :
    cv: Canvas = Canvas(getCanvasSizeFrom(lst))
    return cv

def createRectList (cv: Canvas, lst:list) -> list :
    rectlst = []
    for w in range(len(lst)):
        rectlst.append(Rect(w, lst[w], cv))
    return rectlst

def getIndexOfSortedRect (lst: list, val: int) -> int:
        ind = -1
        i = 0
        nbElem = len(lst)
        while i < nbElem and lst[i].getHeight() <= val and ind == -1:
            if lst[i].getHeight() == val:
                ind = i
            lst[i].setPlaced()
            i += 1
        return ind

def binarySearchRect (lst, val:int) -> int :
    idx = -1
    deb = 0
    fin = len(lst)-1
    while deb <= fin and idx == -1 :
        milieu = (fin + deb) // 2
        mil = lst[milieu].getHeight()
        lst[milieu].setPlaced()
        if mil < val:
            deb = milieu + 1
        elif mil > val:
            fin = milieu - 1
        else:
            idx = milieu
    return idx

