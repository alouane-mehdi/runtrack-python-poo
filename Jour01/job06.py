class Animal:
    def __init__(self, age ):
        self.age = age
        
    def Viellir(self):
        self.age += 1
        
    def nommer(self, prenom) :
        self.prenom = prenom
        print("Le nom de l'animal est", prenom)   
            
        
        
p1 = Animal(0)

print ("L'age de l'animal est de ", p1.age , "an" )

p1.Viellir()

print ("L'age de l'animal est de", p1.age, "an")

p1.nommer("Luna")