class Joueur:
    def __init__(self,nom, numero, position,buts, passes_D,cartons_jaunes,cartons_rouges):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts=buts
        self.passes_D=passes_D
        self.cartons_jaunes=cartons_jaunes
        self.cartons_rouges=cartons_rouges
    def marquerUnBut(self):
        self.buts +=1
    def effectuerUnePasseDecisive(self):
        self.passes_D +=1
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes +=1
    def recevoirUnCartonRouge(self):
        self.cartons_rouges +=1
    def afficherStatistiques(self):
        print(f"Satistiques {self.nom} \nnumero : {self.numero} \nposition: {self.position} \nbut:{ self.buts} \npasses_D :{ self.passes_D} \ncartons_jaunes: {self.cartons_jaunes}\ncartons_rouges : {self.cartons_rouges}")
class Equipe:
    def __init__(self,nom):
        self.nom = nom
        self.liste_joueurs=[]
    def ajouterJoueur(self,joueur):
         self.liste_joueurs.append(joueur)
    def AfficherStatistiquesJoueurs(self): 
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()       
    def mettreAJourStatistiquesJoueur(self,nom, numero, position,buts, passes_D,cartons_jaunes,cartons_rouges):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts=buts
        self.passes_D=passes_D
        self.cartons_jaunes=cartons_jaunes
        self.cartons_rouges=cartons_rouges
Messi=Joueur("Messi",10,"GOAT",5555,5555,0,0)
Payet=Joueur("Payet",10,"Milieu offensif",0,0,0,0)
Pedri=Joueur("Pedri",8,"Milieu",0,0,0,0)
barça=Equipe("barça")
espagne=Equipe("espagne")
barça.ajouterJoueur(Messi)
espagne.ajouterJoueur(Pedri)
barça.ajouterJoueur(Payet)
barça.AfficherStatistiquesJoueurs()
Messi.marquerUnBut()
Payet.effectuerUnePasseDecisive()
Payet.recevoirUnCartonRouge()
Pedri.recevoirUnCartonJaune()
espagne.AfficherStatistiquesJoueurs()