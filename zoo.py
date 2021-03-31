# on crée une nvelle classe qui prend une liste en attribut
#on crée une méthode qui ajoute un objet à une instance de zoo
from animals import *
from oiseau import *
from serpent import *

class Zoo:
    def __init__(self, liste_animaux):
        for animals in liste_animaux:
            if not isinstance(animals,Animal):
                raise ValueError("l'animal doit être une instance de la classe Animal")
        self.liste_animaux=liste_animaux
    def __str__(self):
        lst=""
        for animals in self.liste_animaux:
            lst+=str(animals) + "\n"
        return lst

    def ajoute_animal(self,animal):
        if isinstance(animal,Animal):
            self.liste_animaux.append(animal)

    def __add__(self,other):
        if type(other)==type(self):
            liste_concatenee= self.liste_animaux + other.liste_animaux
            return Zoo(liste_concatenee)
        else:
           raise ValueError("l'animal doit être une instance de la classe Animal")
