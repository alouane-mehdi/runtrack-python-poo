import math
class Forme:
    def aire(self):
        return 0
class Cercle(Forme):
    def __init__(self,radius):
        self.radius=radius
    def aire(self):
        return math.pi*(self.radius*self.radius)
class Rectangle(Forme):
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur
    def aire(self):
        return self.__longueur * self.__largeur
rect=Rectangle(20,10)
print(rect.aire())
cerc=Cercle(20)
print(cerc.aire())