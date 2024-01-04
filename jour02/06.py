class commande:
    def __init__(self,numeroCommande,):
        self.__numeroCommande= numeroCommande
        self.__PlatsCommandes={}
        self.__statutCommande="en cours"
    def ajouterPlat(self,plat,prix):
        self.__PlatsCommandes[plat] = {"prix": prix, "statut": "En cours"}
        print(f"{plat} ajouté à la commande.")
    def annulerCommande(self):
        self.__statutCommande="annulée"
        print("la commande a été annulée")
    def __totalPrix(self):
        total = 0
        for plat, info in self.__PlatsCommandes.items():
            total += info["prix"]
        return total
    def calculerTVA(self):
        total = self.__totalPrix()
        tva=0.7*total
        return tva
    def infoCommande(self):
        print(f"\nLa commande numéro {self.__numeroCommande} : ")
        for plat , info in self.__PlatsCommandes.items():
            print(f"{plat} : {info['prix']} € {info['statut']}")
        total= self.__totalPrix()
        print(f"Total à payer : {total} ({self.calculerTVA()}€ de TVA incluse)")
    

c1=commande(1)
c1.ajouterPlat("pizza",8)
c1.infoCommande()
c1.annulerCommande()
