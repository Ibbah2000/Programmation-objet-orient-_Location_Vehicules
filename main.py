from data_manager import charger_clients, charger_vehicules
from models.tarifs import TarifsManager
from ui import afficher_menu, afficher_liste

def main():
    clients = charger_clients()
    vehicules = charger_vehicules()
    
    while True:
        choix = afficher_menu()
        
        if choix == "1":
            afficher_liste(clients)
        elif choix == "2":
            afficher_liste(vehicules)
        elif choix == "4":
            TarifsManager.afficher_grille()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Option non disponible pour le moment")

if __name__ == "__main__":
    main()





# Question 13

from data_manager import charger_clients, charger_vehicules, charger_reservations, sauvegarder_reservations
from models.tarifs import TarifsManager
from models.reservation import Reservation
from ui import afficher_menu, afficher_liste, saisir_reservation

def main():
    clients = charger_clients()
    vehicules = charger_vehicules()
    reservations = charger_reservations()
    
    while True:
        choix = afficher_menu()
        
        if choix == "1":
            afficher_liste(clients)
        elif choix == "2":
            afficher_liste(vehicules)
        elif choix == "3":
            c, v, d_dep, d_ret, f_km = saisir_reservation(clients, vehicules)
            
            # Pour Calculer automatiquement le prix
            prix_jour, prix_km_supp = TarifsManager.obtenir_tarif(v.cylindree, f_km)
            # Estimation simple : 
            estim = prix_jour * 1.0 
            
            nouvelle_res = Reservation(
                f"RES{len(reservations)+1}", c.id_client, v.id_vehicule,
                d_dep, d_ret, f_km, prix_jour, prix_km_supp, estim
            )
            reservations.append(nouvelle_res)
            sauvegarder_reservations(reservations)
            print("Réservation enregistrée !")
            
        elif choix == "4":
            TarifsManager.afficher_grille()
        elif choix == "5":
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()


