def getPrix(panier:dict, a:str) -> float :
    prix = 0.0
    if a in panier :
        prix =  panier[a]
    return prix

def getPrixTotal(panier:dict) -> float :
    total = 0
    for i in panier :
        total += panier[i]
    return total

def afficherPanier(panier:dict) -> str :

    print(f"{'Articles':^20}{'Prix':>8}")
    print("------------------------------")
    for i in panier :
        print(f"{i:<20} : {panier[i]:>7.2f}")
    print("------------------------------")
    total = getPrixTotal(panier)
    return print(f"{'Prix total':>20} : {total:>7.2f}")

def supprimerArticle(panier:dict, a:str) -> bool :
    opt=False
    a = a.lower()
    a = a.capitalize()
    if a in panier :
        del panier[a]
        opt=True
    return opt

def ajouterArticle(panier:dict, a:str, px:float) -> bool :
    opt=False
    a = a.lower()
    a = a.capitalize()
    if a not in panier :
        panier[a] = px
    else :
        panier[a] += px
    return opt

def getArticlePlusCher(panier:dict) -> str :
    mx = 0
    for i in panier :
        if panier[i] > mx :
            mx = panier[i]
            otp = i
    return otp
