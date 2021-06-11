from BDD_bzb import *
from Classes_bzb import *



#fichier de test
BDD.connect()

lignes = BDD.getLignes()
for ligne in lignes:
    print(ligne.nom_ligne)


arrets = BDD.getArrets()
for arret in arrets:
    print(arret.nom_arret)


bus = BDD.getBus()
for item in bus:
    print(item.numero)