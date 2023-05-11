def  getRandomList (taille:int, mn: int, mx: int) -> list :
    from random import randint
    liste=[]
    for _ in range (taille) :
        nbr = randint(mn, mx)
        liste.append(nbr)
    return liste

def compter (lst:list, elmt:int) -> int :
    nbr=0
    for i in range (len(lst)):
        if elmt == lst[i]:
            nbr+=1
    return nbr

def contient (lst:list, elmt:int) -> bool :
    cnt = False
    for i in range (len(lst)):
        if elmt == lst[i]:
            cnt=True
    return cnt

def firstIndexOf (lst:list, elmt:int) -> int :
    i=0
    pos= -1
    while pos==-1 and i< (len(lst)):
        if elmt == lst[i]:
            pos = i
        i+=1
    return pos

def lastIndexOf (lst:list, elmt:int) -> int :
    pos =-1
    for i in range(len(lst)):
        if elmt == lst[i]:
            pos = i
    return pos

def nthIndexOf (lst:list, n:int, elmt:int) -> int :
    pos = -1
    nbr=0
    i=0
    while nbr<n and i<len(lst):
        if elmt == lst[i]:
            pos = i
            nbr+=1
        i+=1
    if nbr<n:
        return -1
    return pos

def creerListeSansDoublon (lst:list) -> list :
    new_list=[]
    for i in range(len(lst)):
        if not contient(new_list, lst[i]) :
            new_list.append(lst[i])
    return new_list

def supprimerDoublons (lst:list) -> None:
    i=0
    while i < len(lst):
        nbr=compter(lst, lst[i])
        if nbr > 1:
            for _ in range (0, nbr-1):
                del lst[lastIndexOf(lst, lst[i])]
        i+=1
    return None

def enumerer (lst: list,) -> None :
    copy : list = creerListeSansDoublon(lst)
    for i in range (len(lst)) :
        indexes: list = []

        for j in range (len(lst)) :
            idx : nthIndexOf(lst, j, copy[j])

            if idx > -1 :
                indexes.append(idx)

        print(f"Position du {copy[i]} : {indexes}")
    return None