#creation de 2 classes héritant de Animal et modif d'une fonction -> polymorphisme
from animals import *

class Serpent(Animal):
    def se_deplacer(self):
        print("je rampe")

