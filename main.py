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