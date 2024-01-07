class Tache:
    def __init__(self,titre,description):
        self.titre=titre  
        self.description=description
        self.statut="à faire"
    def __str__(self):
        return f"Titre: {self.titre}, Description: {self.description}, Statut: {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.tache=[]
    def ajouterTache(self,LaTache):
        self.tache.append(LaTache)
        print(f"ajout réussit")
    def supprimerTache(self,LaTache):
        self.tache.remove(LaTache)
    def marquerCommeFinie(self,LaTache):
        LaTache.statut = "Fini"
        print(f"{LaTache} finie !")
    def afficherListe(self):
       print("Liste de taches :")
       for tache in self.tache:
            print(tache)
    def filterListe(self,statut):
        n=0
        print(f"les taches {statut} :")
        for task in self.tache:          
            if task.statut == statut:
                n+=1
                print(task)
        if n==0 :
            print("Aucune tache.")

Ranger=Tache("ranger","il faut ranger")
Sortir=Tache("sortir les poubelles","il faut sortir les poubelles")
Nettoyer=Tache("nettoyer","il faut nettoyer")
liste_taches = ListeDeTaches()
liste_taches.ajouterTache(Ranger)
liste_taches.ajouterTache(Sortir)
liste_taches.ajouterTache(Nettoyer)
liste_taches.afficherListe()
liste_taches.supprimerTache(Sortir)
liste_taches.afficherListe()
liste_taches.marquerCommeFinie(Ranger)
liste_taches.afficherListe()
liste_taches.filterListe("à faire")