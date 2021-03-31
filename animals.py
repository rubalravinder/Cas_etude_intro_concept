#creation d'une classe et de son constructeur
# on peut protéger certaines données avec des setter/getter. On le fait pour le poids ici

class Animal:
    def __init__(self,poids,taille):
        self.set_poids(poids) #ici on protège poids
        self.taille=taille

    def se_deplacer(self):
        pass
    
    #getter
    def get_poids(self):
            return self.__poids

    
    #setter
    def set_poids(self,poids):
        if poids>0:
            self.__poids=poids
        else:
            raise ValueError("le poids doit être positif!")
    
    # retourner un str définissant l'objet au cas où on se sait plus ce que c'est par exemple
    def __str__(self):
        return "Classe:"+str(type(self)) +" ,poids:"+str(self.__poids)+"kg ,taille:"+str(self.taille)+"cm"


# dir(OBJET): donne tous les attributs qu'a l'objet (ceux de base dans python et ceux ajoutés)
