from TP5.tp5 import getPrix, getPrixTotal, afficherPanier, supprimerArticle, ajouterArticle, getArticlePlusCher

article : list = ['Pommes','Poires','Fraises','Bananes','Oranges','Clémentines','Endives','Laitues']
prix : list = [5.27, 7.12, 4.98, 3.46, 4.02, 5.27, 1.67, 2.78]
panier = dict(zip(article, prix))


#print(getPrix(panier, "Poires"))
#print(getPrix(panier, "Clémentines"))
#print(getPrix(panier, "Cerises"))

#print(getPrixTotal(panier))

#print(ajouterArticle(panier,'cerises',4.1))

#print(afficherPanier(panier))


panier = { "Pommes": 5.27, "Poires": 7.12, "Fraises": 4.98, "Bananes": 3.46, "Oranges": 4.02, "Clémentines": 5.27, "Endives": 1.67, "Laitues": 2.78 }
print("Liste des articles les plus chers : ")
while len(panier)!=0:
 a = getArticlePlusCher(panier)
 print(f"{a:<20}: prix = {getPrix(panier, a)}")
 supprimerArticle(panier, a)
