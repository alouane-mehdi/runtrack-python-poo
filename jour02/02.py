class livre:
    def __init__(self,titre,auteur,Page):
        self.__titre=titre
        self.__auteur=auteur
        self.__Page=Page
    def modifTitre(self,titre):
        self.titre=titre
    def modifAuteur(self,auteur):
        self.__auteur=auteur
    def modifPage(self,Page):
        if Page >0 :
            self.__Page=Page
        else:
            print("Erreur : La page doit etre un entier positif.")      
    def afficher(self):
        print(f"Titre : {self.__titre} , Auteur: {self.__auteur} , Nombre de page : {self.__Page}. ")
            
l1=livre("Madame Bovary","Gustave Flaubert",468)
l1.afficher()
l1.modifPage(10)
l1.afficher()