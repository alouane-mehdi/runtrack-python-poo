class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
        
    def SePresenter(self):
            return self.nom + self.prenom
        
        
        
p1 = Personne("John", " Doe")  

p2 = Personne("Jean", " Dupond")

print ("Je suis", p1.SePresenter())      
print ("Je suis", p2.SePresenter())

            