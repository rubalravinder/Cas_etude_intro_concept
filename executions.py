from animals import *
from oiseau import *
from serpent import *

#creation d'une instance et print de ses attributs
chat=Animal(5,50)
print(chat.get_poids())
chat.set_poids(45)
print(chat.get_poids())


# On fait des instances des sous-classes et on appelle une de leur méthode
anaconda=Serpent(10,30)
anaconda.se_deplacer()

pie=Oiseau(1,2,400)
pie.se_deplacer()

ferme=Zoo([chat,pie]) # ici les 2 var appartiennent à Animal
print(ferme.liste_animaux)
ferme.ajoute_animal(chat)
print(ferme.liste_animaux)

print(str(chat)) # donne les infos sur l'instance chat

ferme2=Zoo([pie,chat])
ferme3=ferme+ferme2
print(ferme3)
