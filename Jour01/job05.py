class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def afficherLesPoints(self):
            print ("Les coordonnées sont", self.x, self.y)
            
    def afficherX(self):
        print ("La coordonnée X est", self.x)  
        
    def afficherY(self):
        print ("La coordonnée Y est", self.y)    
        
        
    def ChangerX(self, x):
        self.x = x
        print("La nouvelle coordonnée X est", self.x)
    
    def ChangerY(self, y): 
        self.y = y
        print("La nouvelle coordonnée Y est", self.y) 
        
        
                 
            
            
p1 = Point(15, 26)

p1.afficherLesPoints()    

p1.afficherX() 


p1.afficherY()    


p1.ChangerX(200)

p1.ChangerY(250)