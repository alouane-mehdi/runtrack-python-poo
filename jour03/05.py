class Personnage:
    def __init__(self,nom,vie):
        self.nom=nom
        self.vie=vie
    def attaquer(self,ennemi):
        ennemi.vie -= 5
        print(f"vie de {ennemi} : {ennemi.vie}")
    def __str__(self):
        return self.nom


class Jeu:
    def __init__(self):
        self.niveau = 1
        self.joueurs=[]
    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 moyen, 3 difficile) : "))
    def lancerJeu(self):
        self.choisirNiveau()
        if self.niveau == 1:
            joueur=Personnage("joueur",13)
            ennemi=Personnage("ennemi",13)
        if self.niveau == 2:
            joueur=Personnage("joueur",23)
            ennemi=Personnage("ennemi",23)
        if self.niveau == 3:
            joueur=Personnage("joueur",33)
            ennemi=Personnage("ennemi",33)
        
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} n'a plus de vie ! {joueur.nom} remporte la victoire!")
                break
            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} n'a plus de vie ! {ennemi.nom} remporte la victoire!")
                break
jeu=Jeu()
jeu.lancerJeu()