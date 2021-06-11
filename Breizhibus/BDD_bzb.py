import mysql.connector
from Classes_bzb import *

class BDD():

    #Classe de connection à la BDD
    @classmethod
    def connect(cls):
        cls.link = mysql.connector.connect(**{
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'breizhibus',
            'port': '8082'
            })
        cls.cursor=cls.link.cursor()

    #fermeture de la connection
    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.link.close()

    #récupération des lignes de bus
    @classmethod
    def getLignes(cls):
        cls.connect()
        ligneList=[]
        query="SELECT * FROM lignes"
        cls.cursor.execute(query)
        
        for row in cls.cursor.fetchall():
            id_ligne=int(row[0])
            nom_ligne=str(row[1])
            ligne=Ligne(id_ligne, nom_ligne)
            ligneList.append(ligne)
        cls.close()
        return ligneList

    #récupération des arrêts de bus
    @classmethod
    def getArrets(cls, nom_ligne):
        cls.connect()
        arretList=[]
        query="SELECT * FROM `arrets` INNER JOIN arret_ligne ON arrets.id_arret = arret_ligne.id_arret INNER JOIN lignes ON arret_ligne.id_ligne = lignes.id_ligne WHERE nom_ligne ='" + nom_ligne + "'"
        cls.cursor.execute(query)
        
        for row in cls.cursor.fetchall():
            id_arret=int(row[0])
            nom_arret=str(row[1])
            adresse=str(row[2])
            arret=Arret(id_arret, nom_arret, adresse)
            arretList.append(arret)
        cls.close()
        return arretList

    #récupération de la liste des Bus
    @classmethod
    def getBus(cls, nom_ligne):
        cls.connect()
        busList=[]
        query="SELECT * FROM `bus` INNER JOIN lignes ON bus.id_ligne = lignes.id_ligne WHERE nom_ligne = '" + nom_ligne + "'"
        cls.cursor.execute(query)
        
        for row in cls.cursor.fetchall():
            id_bus=int(row[0])
            numero=str(row[1])
            immatriculation=str(row[2])
            nombre_place=str(row[3])
            id_ligne=str(row[4])
            bus=Bus(id_bus, numero, immatriculation, nombre_place, id_ligne)
            busList.append(bus)
        cls.close()
        return busList

    #suppression d'un Bus
    @classmethod
    def supprBus(cls, numero_bus):
        cls.connect()
        query="DELETE FROM bus WHERE numero = %s"  
        param = (numero_bus, )
        cls.cursor.execute(query, param)
        cls.link.commit()
        cls.close()
    
    #Ajout d'un bus
    @classmethod
    def ajouterBus(cls, numero_bus, immatriculation, nombre_place, id_ligne):
        cls.connect()
        query = 'INSERT INTO `bus` (id_bus, numero, immatriculation, nombre_place, id_ligne) VALUES(NULL, %s, %s, %s, %s)'
        param = (numero_bus, immatriculation, nombre_place, id_ligne)
        print(param)
        cls.cursor.execute(query, param)
        cls.link.commit()
        cls.close()