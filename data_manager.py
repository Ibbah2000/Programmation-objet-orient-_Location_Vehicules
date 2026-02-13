import json
import os
from models.client import Client
from models.vehicule import Vehicule

def charger_clients():
    if not os.path.exists("clients.json"):
        return []
    with open("clients.json", "r", encoding="utf-8") as f:
        donnees = json.load(f)
        return [Client.from_dict(d) for d in donnees]

def charger_vehicules():
    if not os.path.exists("vehicules.json"):
        return []
    with open("vehicules.json", "r", encoding="utf-8") as f:
        donnees = json.load(f)
        return [Vehicule.from_dict(d) for d in donnees]
    


# Question 9
def sauvegarder_reservations(reservations):
    with open("reservations.json", "w", encoding="utf-8") as f:
        donnees = [r.to_dict() for r in reservations]
        json.dump(donnees, f, indent=4)


# Question 12
from models.reservation import Reservation

def charger_reservations():
    if not os.path.exists("reservations.json"):
        return []
    with open("reservations.json", "r", encoding="utf-8") as f:
        donnees = json.load(f)
        return [Reservation.from_dict(d) for d in donnees]        