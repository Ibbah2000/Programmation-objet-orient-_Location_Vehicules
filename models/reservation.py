from datetime import datetime

class Reservation:
    def __init__(self, id_reservation, id_client, id_vehicule, date_depart, date_retour, forfait_km, cout_journalier, prix_km_supp, cout_estime=None):
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_vehicule = id_vehicule
        self.date_depart = date_depart
        self.date_retour = date_retour
        self.forfait_km = forfait_km
        self.cout_journalier = cout_journalier
        self.prix_km_supp = prix_km_supp
        
        if cout_estime is None:
            self.cout_estime = self._calculer_cout_estime()
        else:
            self.cout_estime = cout_estime

    def _calculer_cout_estime(self):
        fmt = "%d/%m/%Y"
        try:
            d1 = datetime.strptime(self.date_depart, fmt)
            d2 = datetime.strptime(self.date_retour, fmt)
            nb_jours = (d2 - d1).days
            if nb_jours < 1: 
                nb_jours = 1
            
            return nb_jours * self.cout_journalier
        except ValueError:
            return 0.0

    def __str__(self):
        return (f"Réservation {self.id_reservation} | Client: {self.id_client} | "
                f"Véhicule: {self.id_vehicule} | Total: {self.cout_estime}€")

    def to_dict(self):
        return {
            "id_reservation": self.id_reservation,
            "id_client": self.id_client,
            "id_vehicule": self.id_vehicule,
            "date_depart": self.date_depart,
            "date_retour": self.date_retour,
            "forfait_km": self.forfait_km,
            "cout_journalier": self.cout_journalier,
            "prix_km_supp": self.prix_km_supp,
            "cout_estime": self.cout_estime
        }

    @staticmethod
    def from_dict(data):
        return Reservation(
            data['id_reservation'], data['id_client'], data['id_vehicule'],
            data['date_depart'], data['date_retour'], data['forfait_km'],
            data['cout_journalier'], data['prix_km_supp'], data['cout_estime']
        )