class Ville :
    def __init__(self, nom, nbhabitants):
        self.__nom = nom
        self.__nbhabitants = nbhabitants
        
    def get_nom(self):
        return  self.__nom 
    
    def get_nbhabitants(self):
        return self.__nbhabitants  
    
    def set_nbhabitants(self, nbhabitants):
        self.__nbhabitants=nbhabitants
         
 
        
class Personne : 
    def __init__(self, nom, age, obj):
        self.__nom = nom
        self.__age = age
        self.__obj = obj


    def ajouterPopulation(self):
        add= Ville.get_nbhabitants() 
        
        
        
v1 = Ville("Paris", 1000000)

print("Population de la ville de", v1.get_nom(), ":", v1.get_nbhabitants())   
    
    
v2 = Ville("Marseille", 861635)

print("Population de la ville de", v2.get_nom(), ":", v2.get_nbhabitants())


       
p1 = Personne("John", 45, v1)

p2 = Personne("Myrtille", 4, v1)

p3 = Personne("Chloé", 18, v1)


print("Mise a jour", v1.get_nbhabitants())

           