#creation d'une classe et de son constructeur
# on peut protéger certaines données avec des setter/getter. On le fait pour le poids ici

class Animal:
    def __init__(self,poids,taille):
        self.__poids=poids #ici on protège poids
        self.taille=taille

    def se_deplacer(self):
        pass
    
    #getter
    def get_poids(self):
        if self.__poids>0:
            return self.__poids
        else:
            raise ValueError("le poids doit être positif!")
    
    #setter
    def set_poids(self,poids):
        self.__poids=poids
    
    # retourner un str définissant l'objet au cas où on se sait plus ce que c'est par exemple
    def __str__(self):
        return "Classe:"+str(type(self)) +" ,poids:"+str(self.__poids)+"kg ,taille:"+str(self.taille)+"cm"

#creation d'une instance et print de ses attributs
chat=Animal(5,50)
print(chat.get_poids())
chat.set_poids(45)
print(chat.get_poids())

#creation de 2 classes héritant de Animal et modif d'une fonction -> polymorphisme
class Serpent(Animal):
    def se_deplacer(self):
        print("je rampe")

# On fait des instances des sous-classes et on appelle une de leur méthode
anaconda=Serpent(10,30)
anaconda.se_deplacer()

# on ajoute un nouvel attribut à la classe oiseau en utilisant le mot-clé super
# on peut protéger certaines données avec des setter/getter. On le fait pour le poids ici
class Oiseau(Animal):
    def __init__(self,poids,taille,altitude_max):
        super().__init__(poids,taille)
        self.altitude_max=altitude_max

    def se_deplacer(self):
        print("je vole")

pie=Oiseau(1,2,400)
pie.se_deplacer()

# dir(OBJET): donne tous les attributs qu'a l'objet (ceux de base dans python et ceux ajoutés)


# on crée une nvelle classe qui prend une liste en attribut
#on crée une méthode qui ajoute un objet à une instance de zoo

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



ferme=Zoo([chat,pie]) # ici les 2 var appartiennent à Animal
print(ferme.liste_animaux)
ferme.ajoute_animal(chat)
print(ferme.liste_animaux)

print(str(chat)) # donne les infos sur l'instance chat

ferme2=Zoo([pie,chat])
ferme3=ferme+ferme2
print(ferme3)
