class livre:
    def __init__(self,titre,auteur,Page):
        self.titre=titre
        self.auteur=auteur
        self.Page=Page
    def modifTitre(self,titre):
        self.titre=titre
    def modifAuteur(self,auteur):
        self.auteur=auteur
    def modifPage(self,Page):
        if Page >0 :
            self.Page=Page
        else:
            print("Erreur : La page doit etre un entier positif.")      
    def afficher(self):
        print(f"Titre : {self.titre} , Auteur: {self.auteur} , Nombre de page : {self.Page}. ")
l1=livre("Madame Bovary","Gustave Flaubert",468)
l1.afficher()
l1.modifPage(10)
l1.afficher()