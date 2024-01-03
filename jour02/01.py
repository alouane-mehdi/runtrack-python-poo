class rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur
    def mutateur(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur
    def afficher(self):
        print(f"longueur : {self.__longueur} , largeur: {self.__largeur}")
r1=rectangle(25,10)
r1.afficher()
r1.mutateur(10,5)
r1.afficher()
