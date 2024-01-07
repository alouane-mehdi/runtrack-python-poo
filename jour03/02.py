class compteBancaire:
    def __init__(self,numcompte,prenom,nom,solde, decouvert):
        self.__numcompte = numcompte
        self.__prenom = prenom
        self.__nom = nom
        self.__solde = solde
        self.__decouvert = decouvert  
    def afficher(self):
        print("Numéro de compte :", self.__numcompte, "Prénom :", self.__prenom, "Nom :", self.__nom, "solde :", self.__solde)
        
    def afficherSolde(self):
        print("Solde :",self.__solde)  
        
    def versement(self, montant):
        self.__montant = montant
        self.__solde += montant
        print("Nouveau Solde :", self.__solde)
         
    def retrait(self, Rmontant):
        self.__Rmontant = Rmontant
        if Rmontant >= self.__solde:
            print("Erreur, Montant indisponible")
        else:    
            self.__solde -= Rmontant
            print("Nouveau Solde :", self.__solde)  
            
    def agios(self) : 
        if self.__solde < 0:
            self.__solde -= 5

    def virement(self,reference,compteBancaire,montant):
        reference.afficherSolde()
        compteBancaire.afficherSolde()
        if montant < compteBancaire.__solde:
            compteBancaire.__solde -= montant
            reference.__solde += montant
            print(f"virement éffectué !")
            reference.afficherSolde()
            compteBancaire.afficherSolde()
        else:
            print("Il n'y a pas assez de sous")          
        
                  
        
        
cb = compteBancaire(1, "John", "Doe", 145, True)  

cb.afficher()     

cb.afficherSolde()

cb.versement(50)

cb.retrait(700)

cb2 = compteBancaire(2, "John", "Deux", 150, True)

cb2.virement(cb, cb2, 450)



