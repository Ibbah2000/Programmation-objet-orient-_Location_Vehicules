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