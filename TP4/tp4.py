from random import randint

def getRegularArray2D (nl:int, nc:int, mn:int, mx:int) -> list : 
    lgn :list = []
    for i in range (nl):
        col :list = []
        for j in range (nc) :
            col.append(randint(mn,mx))
        lgn.append(col)
    return lgn

def isRegular (lst:list) -> bool :
    nbElem = len(lst)-1
    otp :bool = True
    i :int = 0

    while i < nbElem and otp:
        if len(lst[i]) != len(lst[i+1]) :
            otp =False
        i += 1

    return otp

def getMin (lst:list) -> int :
    nbElem = len(lst)
    mn = min(lst[0])

    for i in range (nbElem) :

        if mn > min(lst[i]):
            mn = min(lst[i])

    return mn

def getMax (lst:list) -> int :
    nbElem = len(lst)
    mx = max(lst[0])

    for i in range (nbElem) :

        if mx < max(lst[i]):
            mx = max(lst[i])

    return mx

def getSize2D(lst:list) -> tuple :
    nl = len(lst)
    nc=len(lst[0])
    return (nl, nc)

def getCarre2D (n:int) -> list :
    from random import shuffle, randint
    lgn :list = []
    ints : list = []
    for x in range (1, (n**2)+1):
        ints.append(x)

    shuffle(ints)

    for i in range (n):
        col :list = []
        for j in range (n) :
            col.append(ints.pop())
        lgn.append(col)

    return lgn

def getSommeLignes (tab:list) -> list :
    lst : list = []
    nbElem = len(tab)
    for i in range (nbElem):
        lst.append(sum(tab[i]))
    return lst

def getSommeColonnes(tab:list) -> list :
    lst : list = []
    total = 0
    nbElem = len(tab)
    for i in range (nbElem) :
        for j in range (nbElem) :
            total += tab[j][i]
        lst.append(total)
        total = 0
    return lst

def getSommeDiagonale1(tab:list) -> int :
    nbElem = len(tab)
    total = 0
    for i in range (nbElem) :
        total += tab[i][i]
    return total

def getSommeDiagonale2(tab:list) -> int :
    nbElem = len(tab)
    total = 0
    for i in range (nbElem) :
        total += tab[i][nbElem-1-i]
    return total

def dessinerCarre(tab:list) -> Canvas :
    from view.Text import Text
    mx = getMax(tab)
    diag1 = getSommeDiagonale1(tab)
    diag2 = getSommeDiagonale2(tab)
    col = getSommeColonnes(tab)
    lgn = getSommeLignes(tab)
    txt = Text((0, 0), str(n))
    w, h = txt.getSize()
    # Ajout de la marge h/2
    w += h
    h += h
    # Taille des cadres pour les nombres : (w, h)

    cv: Canvas = Canvas((len(tab)*w +2 * w, len(lst[0]) *h +h))

    cv.drawFrame(0x55555)
    y=0
    for r in range (len(lst)):
        x = w
        for c in range(len(lst[r])):
            tr : TextRect = TextRect((x,y), str(lst[r][c]), rect=(w,h))

            tr.setFill(0xFFFFFF) #white
            cv.draw(tr)

            x+=w

        tr : TextRect =TextRect((x,y), str(lgn[r]), rect=(w,h))

        tr.noFill()
        tr.noStroke()
        cv.draw(tr)

        y += h

        for row in lst:
            x=0
            tr: TextRect = TextRect((x, y), str(diag2), rect=(w, h))

            tr.noFill()
            tr.noStroke()
            cv.draw(tr)

            x += w

            for c in range(len(row):
                tr: TextRect = TextRect((x, y), str(col[c]), rect=(w, h))

                tr.noFill()
                tr.noStroke()
                cv.draw(tr)

                x += w

            tr: TextRect = TextRect((x, y), str(diag1), rect=(w, h))

            tr.noFill()
            tr.noStroke()
            cv.draw(tr)

        return cv

def zeros(nl:int, nc:int) -> list :
    tab : list = []
    for i in range (nl):
        row : list = []
        for j in range (nc):
            row.append(0)
        tab.append(row)
    return tab


def creerCarremagique(n:int) -> list :
    tab = zeros(n,n)
    x = 0
    y = int((n + 1) / 2 - 1)
    tab[x][y] = 1

    for i in range(2, n * n + 1):
        x_old = x
        y_old = y

        if x == 0:
            x = n - 1
        else:
            x -= 1

        if y == n - 1:
            y = 0
        else:
            y += 1

        while tab[x][y] != 0:
            if x == n - 1:
                x = 0
            else:
                x = x_old + 1
            y = y_old

        tab[x][y] = i

    return tab

def getArray2D(lst:list) -> list :
    tab : list = []
    nbElem = len(lst)
    for i in range (nbElem) :
        lgn : list = []
        for j in range (lst[i]):
            lgn.append(0)
        tab.append(lgn)
    return tab

def getNbParLigne(tab:list) -> list :
    lst : list = []
    nbElem = len(tab)
    for i in range (nbElem):
        lst.append(len(tab[i]))
    return lst

def remplir2D(tab:list, mn:int, mx:int) -> None :
    from random import randint
    nbElem = len(tab)
    for i in range (nbElem):
        nbSubElem = len(tab[i])
        for j in range (nbSubElem) :
            nb = randint(mn, mx)
            tab[i][j] = nb
    return None

def copyArray2D(tab:list) -> list :
    cop : list = []
    nbElem = len(tab)
    for i in range (nbElem) :
        row : list = []
        for j in range (len(tab[i])):
            row.append(tab[i][j])
        cop.append(row)
    return cop

def transforme2D1D(tab:list) -> list :
    lst :list = []
    nbElem = len(tab)
    for i in range (nbElem):
        for j in range (len(tab[i])):
            lst.append(tab[i][j])
    return lst

def transforme1D2D(lst:list, sep:int) -> list :
    tab : list = []
    nbElem = len(lst)
    i = 0
    while i <= nbElem :
        l : list = []
        while i < nbElem and lst[i] != sep:
            l.append(lst[i])
            i += 1
        tab.append(l)
        i += 1
    return tab
