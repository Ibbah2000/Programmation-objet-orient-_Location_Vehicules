def afficher_menu():
    """ Affiche les options principales de l'application """
    print(" MENU LOCATION VÉHICULES ")
    print(" Liste des clients")
    print(" Liste des véhicules")
    print(" Créer une réservation")
    print(" Afficher la grille tarifaire")
    print(" Quitter")
    return input("Votre choix : ")

def afficher_liste(objets):
    for obj in objets:
        print("-" * 20)
        print(obj)



def saisir_reservation(clients, vehicules):
    """ Permet de saisir les informations d'une nouvelle réservation """
    print(" NOUVELLE RÉSERVATION")
    
    for i, c in enumerate(clients):
        print(f"{i}. {c.prenom} {c.nom}")
    index_client = int(input("Choisissez l'index du client : "))
    client_choisi = clients[index_client]

    for i, v in enumerate(vehicules):
        print(f"{i}. {v.marque} {v.modele}")
    index_veh = int(input("Choisissez l'index du véhicule : "))
    vehicule_choisi = vehicules[index_veh]

    date_dep = input("Date de départ (JJ/MM/AAAA) : ")
    date_ret = input("Date de retour (JJ/MM/AAAA) : ")
    forfait = int(input("Forfait km (100, 200, 300 ou 400 pour +300) : "))
    
    return client_choisi, vehicule_choisi, date_dep, date_ret, forfait  

# Question 14
def afficher_menu():
    print(" MENU LOCATION VÉHICULES")
    print("1. Liste des clients")
    print("2. Liste des véhicules")
    print("3. Créer une réservation")
    print("4. Liste des réservations")
    print("5. Bilan de l'agence")
    print("6. Afficher la grille tarifaire")
    print("7. Quitter")
    return input("Votre choix : ")      