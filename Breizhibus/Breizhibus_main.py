from BDD_bzb import *
from Classes_bzb import *
import tkinter.messagebox
import tkinter as tk
from functools import partial

class Application(tk.Tk):

  def __init__(self):
        
    tk.Tk.__init__(self)
    self.geometry("1300x760")
    self.create_widget()
    self.v=tk.IntVar()


  def create_widget(self):
              
    self.menubar = tk.Menu(self)
    self.config(menu=self.menubar)


    """Titre"""
    self.champ_titre=tk.Label(self,text="Projet Breizhibus",padx="10",pady="10")
    self.champ_titre.config(font=("Helvetica", 44), fg='#7be50a')
    self.champ_titre.pack(side="top")

    """Appel des fonctions"""
    self.pageAcceuil()
    self.choixLigne()

  def pageAcceuil(self):
    """Fenêtre principale"""
    self.appli=tk.Frame(self)
    self.appli.config(bg = '#8afe0f')
    self.appli.pack(fill ="both", expand="yes")

  """Fenêtre d'affichage de la liste des lignes"""
  def choixLigne(self):
    #Le titre
    for widget in self.appli.winfo_children():
      widget.destroy()
    self.ligneTitre = tk.Label(self.appli, text="Choisissez votre ligne", pady="20")
    self.ligneTitre.config(font=("Helvetica", 25), fg='white', bg = '#8afe0f')
    self.ligneTitre.pack(side = "top")
    #La Frame
    self.ligneFrame = tk.Frame(self.appli)
    self.ligneFrame.pack(expand="yes")
    self.listeLigne()

    self.appli.pack(fill ="both", expand="yes")

  #Les boutons de choix de lignes
  def listeLigne(self):

    self.liste_ligne = BDD.getLignes()
    for ligne in self.liste_ligne:
      tk.Button(self.ligneFrame, text=ligne.nom_ligne, height=5, width=15, bd=5, bg='#eaeaea', activebackground='#c8c8c8', command=partial(self.pageLigne, ligne.nom_ligne)).pack()

  """Page d'affichage des arrêts en fonction de la ligne choisi"""
  def pageLigne(self, titre_ligne):
    for widget in self.appli.winfo_children():
      widget.destroy() 
    self.titre_ligne = titre_ligne
    if self.titre_ligne == 'Rouge':
      color = 'red'
    elif self.titre_ligne == 'Vert':
      color = 'green'
    else:
      color = 'blue'
    self.titreLigne = tk.Label(self.appli, text=f"Vous avez choisi la ligne {self.titre_ligne}", pady="20")
    self.titreLigne.config(font=("Helvetica", 25), fg = color, bg = '#8afe0f')
    self.titreLigne.pack(side = "top")
    # Bouton de retour
    self.boutonRetour = tk.Button(self.appli, text='Retour', height=1, width=5, bd=5, bg='#eaeaea', activebackground='#c8c8c8', command=partial(self.choixLigne))
    self.boutonRetour.pack()

    self.sousTitreLigne = tk.Label(self.appli, text = "Liste des arrêts")
    self.sousTitreLigne.config(font=("Helvetica", 25), fg = 'white', bg = '#8afe0f')
    self.sousTitreLigne.pack(side = "top")
    #Je récupère la liste des arret en fonction de la ligne choisi
    self.listeArrets = BDD.getArrets(self.titre_ligne)
    for arret in self.listeArrets:
      self.nomArretFrame = tk.Label(self.appli, text=arret.nom_arret, pady="20", width=20, height=3, bd=1, relief='sunken')
      self.nomArretFrame.pack()
    #je récupère la liste des bus en fonction de la ligne choisi
    self.liste_bus(self.titre_ligne)


  '''fonction qui récupère la liste des bus'''
  def liste_bus(self, titre_ligne):
    if self.titre_ligne == 'Rouge':
      color = 'red'
    elif self.titre_ligne == 'Vert':
      color = 'green'
    else:
      color = 'blue'
    self.titreBus = tk.Label(self.appli, text=f"Voici le(s) bus de la ligne {self.titre_ligne}", pady="10",padx="30", bg = '#8afe0f' ,fg= color, font=("Helvetica", 15,))
    self.titreBus.pack()
    self.listeBus = BDD.getBus(self.titre_ligne)
    for bus in self.listeBus:
      self.busFrame = tk.Label(self.appli, text=bus.numero, pady="20", width=20, height=3, bd=1, relief='sunken')
      self.busFrame.pack(ipadx=25, ipady=25)
      self.BoutonSupprBus = tk.Button(self.busFrame, text = 'Supprimer', command=lambda bus=bus: BDD.supprBus(bus.numero))
      self.BoutonSupprBus.pack(side = 'bottom')
    self.boutonAjoutBus = tk.Button(self.appli, text='ajouter bus', pady = '20', padx = '20', bg='silver', command = lambda: self.ajouter_bus(self.titre_ligne))
    self.boutonAjoutBus.pack(side = 'top')

  '''fonction qui ajoute la page "ajouter bus"'''
  def ajouter_bus(self, titre_ligne):
    for widget in self.appli.winfo_children():
      widget.destroy()
    self.titre_ligne = titre_ligne
    if self.titre_ligne == 'Rouge':
      color = 'red'
    elif self.titre_ligne == 'Vert':
      color = 'green'
    else:
      color = 'blue'
    self.ajoutBusFrame = tk.Frame(self.appli)
    self.ajoutBusFrame.pack()
    self.ajoutBusFrameTitre = tk.Label(self.ajoutBusFrame, text=f'Ajouter un bus à la ligne {self.titre_ligne}')
    self.ajoutBusFrameTitre.config(font=("Helvetica", 25), fg = color, bg = '#8afe0f')
    self.ajoutBusFrameTitre.pack()

    # Bouton de retour
    self.boutonRetour2 = tk.Button(self.appli, text='Retour à la liste des lignes', height=1, width=25, bd=5, bg='#eaeaea', activebackground='#c8c8c8', command=partial(self.choixLigne))
    self.boutonRetour2.pack()

    #formulaire
    self.formulaire1Titre = tk.Label(self.appli, text="Numéro du Bus")
    self.formulaire1 = tk.Entry(self.appli, textvariable=tk.StringVar)
    self.formulaire1Titre.pack()
    self.formulaire1.pack()

    self.formulaire2Titre = tk.Label(self.appli, text="Immatriculation du Bus")
    self.formulaire2 = tk.Entry(self.appli, textvariable=tk.StringVar)
    self.formulaire2Titre.pack()
    self.formulaire2.pack()

    self.formulaire3Titre = tk.Label(self.appli, text="Nombre de places")
    self.formulaire3 = tk.Entry(self.appli, textvariable=tk.StringVar)
    self.formulaire3Titre.pack()
    self.formulaire3.pack()

    #bouton de validation
    if self.titre_ligne == 'Rouge':
      self.idBus = 1
    elif self.titre_ligne == 'Vert':
      self.idBus = 2
    else:
      self.idBus = 3
    self.boutonValideBus = tk.Button(self.appli, text='ajouter bus', pady = '20', padx = '20', bg='silver', command = lambda: BDD.ajouterBus(self.formulaire1.get(), self.formulaire2.get(), self.formulaire3.get(), self.idBus))
    self.boutonValideBus.pack()

def breizhibus():

  app=Application()
  app.mainloop()


breizhibus()