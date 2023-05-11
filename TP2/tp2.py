def estTrie (lst: list) -> bool :
    i = 0
    outp = True
    lenlst=(len(lst)-1)
    while i < lenlst and outp:
        if lst[i] > lst[i+1]:
            outp=False
        i+=1
    return outp

def echanger (lst: list, i1: int ,i2: int) -> None :
    lst[i1], lst[i2] = lst[i2], lst[i1]
    return None

def triBulles (lst : list) -> None :
    while not estTrie(lst):
        for j in range (len(lst)-1):
            if lst[j] > lst[j+1]:
                echanger(lst, j, j+1)

def getMin (lst: list) -> int:
    min=lst[0]
    for i in range (1, len(lst)):
        if lst[i]<min:
            min=lst[i]
    return min

def getIndexMin (lst: list) -> int:
    min=lst[0]
    index=0
    for i in range (1, len(lst)):
        if lst[i]<min:
            min=lst[i]
            index=i
    return index

def getIndexMinFrom (lst: list, dep: int) -> int :
    min=lst[dep]
    index=dep
    for i in range (dep, len(lst)):
        if lst[i]<min:
            min=lst[i]
            index=i
    return index

def triSelection (lst: list) -> None :
    for i in range (len(lst)) :
        min=getIndexMinFrom(lst, i)
        echanger(lst, i, min)
    return None

def deplacerCase (lst: list, indice: int) -> None :
    while lst[indice]<lst[indice-1] and indice > 0:
        lst[indice], lst[indice-1] = lst[indice-1], lst[indice]
        indice-=1
    return None

def triInsertion (lst: list) -> None :
    for i in range (len(lst)) :
        deplacerCase(lst, i)
    return None

def echangerRect (lst: list, i1: int, i2: int, tps: float) -> None :
    tmp = lst[i1]
    tmp.unsetX(tps)
    lst[i1] = lst[i2]
    lst[i1].setX(i1, tps)
    lst[i2] = tmp
    lst[i2].setX(i2, tps)
    return None

def estTrieRect (lst: list) -> bool :
    i = 0
    outp = True
    nbElem=(len(lst)-1)
    while i < nbElem and outp:
        if lst[i].getHeight() > lst[i+1].getHeight():
            outp=False
        i+=1
    return outp

def triSelectionRect (lst: list, tps: float) -> None :
    for j in range (len(lst)) :
        mini: float = lst[j].getHeight()
        index = j
        for i in range(j, len(lst)):
            if lst[i].getHeight() < mini:
                mini = lst[i].getHeight()
                index = i
        echangerRect(lst, j, index, tps)

    return None

def triBullesRect (lst:list, tps:float) -> None :
    while not estTrieRect(lst):
        for j in range (len(lst)-1):
            if lst[j].getHeight() > lst[j+1].getHeight():
                echangerRect(lst, j, j+1, tps)

def deplacerCaseRect (lst: list, indice: int, tps: float) -> None :
    while lst[indice].getHeight() < lst[indice-1].getHeight() and indice > 0:
        echangerRect(lst, indice, indice-1, tps)
        indice-=1
    return None

def triInsertionRect (lst: list, tps:float) -> None :
    for i in range (len(lst)) :
        deplacerCaseRect(lst, i, tps)
    return None

def doQuickSort (lst:list, ideb:int, ifin:int) -> None :
    pivot = ideb
    _ideb = ideb
    _ifin = ifin
    while _ideb < _ifin:
        while lst[_ifin] > lst[pivot]:
            _ifin -= 1
        while _ideb < _ifin and lst[_ideb] <= lst[pivot] :
            _ideb += 1
        if _ideb < _ifin:
            echanger(lst, _ideb, _ifin)
    if _ifin != pivot:
        echanger(lst, _ifin, pivot)
        pivot = _ifin
    if pivot-ideb > 1:
        doQuickSort(lst, ideb, (pivot-1))
    if ifin-pivot > 1:
        doQuickSort(lst, (pivot+1), ifin)
    return None

def quickSort (lst:list) -> None :
    nbElem = len(lst)-1
    doQuickSort(lst,0,nbElem)
    return None

def doQuickSortRect (lst:list, ideb:int, ifin:int, tps: float) -> None :
    pivot = ideb
    _ideb = ideb
    _ifin = ifin
    while _ideb < _ifin:
        while lst[_ifin].getHeight() > lst[pivot].getHeight():
            _ifin -= 1
        while _ideb < _ifin and lst[_ideb].getHeight() <= lst[pivot].getHeight():
            _ideb += 1
        if _ideb < _ifin:
            echangerRect(lst, _ideb, _ifin, tps)
    if _ifin != pivot:
        echangerRect(lst, _ifin, pivot, tps)
        pivot = _ifin
    if pivot-ideb > 1:
        doQuickSortRect(lst, ideb, (pivot-1), tps)
    if ifin-pivot > 1:
        doQuickSortRect(lst, (pivot+1), ifin, tps)
    return None

def quickSortRect (lst:list, tps: float) -> None :
    nbElem = len(lst)-1
    doQuickSortRect(lst,0,nbElem, tps)

