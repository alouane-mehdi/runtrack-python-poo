class personnage:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def haut(self):
        self.y-=5
    def bas(self):
        self.y+=5
    def gauche(self):
        self.x-=5
    def droit(self):
        self.x+=5
    def position(self):
        print(f"({self.x} {self.y})")
        
p1 = personnage(200, 500)
p1.position()
p1.haut()
p1.droit()
p1.droit()
p1.position()
        