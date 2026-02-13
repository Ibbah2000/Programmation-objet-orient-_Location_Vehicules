import json
import os
from models.client import Client
from models.vehicule import Vehicule
from models.reservation import Reservation

# Questions 07, 12 et 16

def charger_clients():
    if not os.path.exists("clients.json"):
        return []
    try:
        with open("clients.json", "r", encoding="utf-8") as f:
            donnees = json.load(f)
            return [Client.from_dict(d) for d in donnees]
    except (json.JSONDecodeError, IOError):
        print("Erreur : Impossible de lire clients.json (fichier corrompu ou inaccessible).")
        return []

def charger_vehicules():
    if not os.path.exists("vehicules.json"):
        return []
    try:
        with open("vehicules.json", "r", encoding="utf-8") as f:
            donnees = json.load(f)
            return [Vehicule.from_dict(d) for d in donnees]
    except (json.JSONDecodeError, IOError):
        print("Erreur : Impossible de lire vehicules.json.")
        return []

def charger_reservations():
    if not os.path.exists("reservations.json"):
        return []
    try:
        with open("reservations.json", "r", encoding="utf-8") as f:
            donnees = json.load(f)
            return [Reservation.from_dict(d) for d in donnees]
    except (json.JSONDecodeError, IOError):
        print("Erreur : Impossible de lire reservations.json.")
        return []

#SAUVEGARDE ET FILTRAGE

def sauvegarder_reservations(reservations):
    try:
        with open("reservations.json", "w", encoding="utf-8") as f:
            donnees = [r.to_dict() for r in reservations]
            json.dump(donnees, f, indent=4)
    except IOError:
        print("Erreur : Impossible d'écrire dans reservations.json.")

def filtrer_reservations_par_client(reservations, id_client):
    """ Question 12 : Retourne les réservations d'un client spécifique """
    return [r for r in reservations if r.id_client == id_client]