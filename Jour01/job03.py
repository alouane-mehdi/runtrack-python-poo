class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition(self):
        resultat = self.nombre1 + self.nombre2  
        print (resultat)      
        
p1 = Operation(15, 17)

p1.addition()


