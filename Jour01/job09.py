class produit:
    def __init__(self,nom, prixHT,TVA):
        self.nom=nom
        self.prixHT=prixHT
        self.TVA= TVA
    def CalculerPrixTTC(self):
        prixTTC = self.prixHT + (self.prixHT * (self.TVA / 100))
        return prixTTC
    def afficher(self):
        infos= f"nom : {self.nom} , prix TTC : {self.CalculerPrixTTC()}"
        return infos
    def ChangerNom(self,nom):
        self.nom = nom
    def ChangerPrixHT(self,prixHT):
        self.prixHT=prixHT
    
p1=produit("bonbons",5,2)
p1.ChangerPrixHT(2)
print(p1.afficher())
p2=produit("cola",2,1)
p2.ChangerNom("soda")
print(p2.afficher())
p3=produit("gateau",4,2)
print(p3.afficher())