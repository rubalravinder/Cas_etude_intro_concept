# on ajoute un nouvel attribut à la classe oiseau en utilisant le mot-clé super
# on peut protéger certaines données avec des setter/getter. On le fait pour le poids ici
from animals import *
from zoo import Zoo

class Oiseau(Animal):
    def __init__(self,poids,taille,altitude_max):
        super().__init__(poids,taille)
        self.altitude_max=altitude_max

    def se_deplacer(self):
        print("je vole")
