# Système de Location de Véhicules

## Spécification des classes

### Client
- Attributs : id_client, nom, prenom, mail, telephone, adresse
- Rôle : Représente les informations d'un client de l'agence.

### Vehicule
- Attributs : id_vehicule, marque, modele, cylindree, kilometrage_actuel, date_mise_en_circulation
- Rôle : Stocke les caractéristiques techniques des véhicules.

### Reservation
- Attributs : id_reservation, id_client, id_vehicule, date_depart, date_retour, forfait_km, cout_journalier, prix_km_supp, cout_estime
- Rôle : Lie un client à un véhicule et calcule les coûts de location.