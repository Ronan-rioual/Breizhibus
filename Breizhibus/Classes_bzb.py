class Bus():
    def __init__(self, id_bus, numero, immatriculation, nombre_place, id_ligne):
        self.id_bus = id_bus
        self.numero = numero
        self.immatriculation = immatriculation
        self.nombre_place = nombre_place
        self. id_ligne = id_ligne


class Ligne():
    def __init__(self, id_ligne, nom_ligne):
        self.id_ligne = id_ligne
        self.nom_ligne = nom_ligne


class Arret():
    def __init__(self, id_arret, nom_arret, adresse):
        self.id_arret = id_arret
        self.nom_arret = nom_arret
        self.adresse = adresse