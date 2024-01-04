class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche

    def marque(self, marque):
        self.__marque = marque

    def modele(self, modele):
        self.__modele = modele

    def annee(self, annee):
        self.__annee = annee

    def kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def en_marche(self, en_marche):
        self.__en_marche = en_marche

  
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def demarrer(self):
        self.__en_marche = True
        print("La voiture démarre.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est à l'arrêt.")

ma_voiture = Voiture("Audi", "RS3", 2013, 20000)



ma_voiture.en_marche(True)
print(ma_voiture.get_marque())

