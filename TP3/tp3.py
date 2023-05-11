def indexOf (lst:list, val:int) -> int:
    ind=-1
    i=0
    nbElem=len(lst)
    while ind==-1 and i<nbElem :
        if lst[i]==val:
            ind=i
        i+=1
    return ind

def indexOfSorted (lst:list, val:int) -> tuple:
    ind=-1
    i=0
    nbElem=len(lst)
    while i<nbElem and lst[i]<=val and ind==-1:
        if lst[i]==val :
            ind=i
        i+=1
    return (ind,i)

def binarySearch(lst:list, val:int) -> int:
    deb = 0
    fin = len(lst)-1
    otp=-1
    while deb <= fin and otp == -1 :
        milieu = (fin + deb) // 2

        if lst[milieu] < val:
            deb = milieu + 1
        elif lst[milieu] > val:
            fin = milieu - 1
        else:
            otp = milieu
    return otp
 

def getReponse (val: int) -> str :
    print("Proposition de l'ordinateur : ", val)
    otp : str = input("Votre nombre est-il (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P) : ")
    otp = otp.upper()
    while otp not in ("E","G","P"):
        otp : str = input("Votre nombre est-il (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P) : ")
        otp = otp.upper()
    return otp

def devinerNombre (mn:int,mx:int) -> str :
    sol=input(f"Choisissez un nombre entre {mn} et {mx}...")
    otp = ""
    guess = (mn+mx)//2
    rep = getReponse(guess)
    nbGuess=0
    while guess!=sol and rep==E:
        guess = (mn+mx)//2
        rep=getReponse(guess)
        if rep=="E":
            otp = f"ଘ(੭ ˘ ᵕ˘)━☆ﾟ.*･｡ﾟᵕ꒳ᵕ~ Trouvé en {nbGuess} essais"
        elif rep=="G":
            mn=guess+1
        else:
            mx=guess-1
        if nbGuess > (mx/2)/2: 
            otp = "Je n’ai pas trouvé !?"
        nbGuess+=1
    return otp
    
