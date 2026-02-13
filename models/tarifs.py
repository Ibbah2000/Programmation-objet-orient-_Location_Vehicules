class TarifsManager:
    TARIFS = {
        4: {
            100: (35.0, 0.25), 200: (50.0, 0.20), 
            300: (65.0, 0.15), "+300": (80.0, 0.10)
        },
        5: {
            100: (45.0, 0.30), 200: (60.0, 0.25), 
            300: (75.0, 0.20), "+300": (95.0, 0.15)
        },
        6: {
            100: (60.0, 0.40), 200: (80.0, 0.35), 
            300: (100.0, 0.30), "+300": (120.0, 0.25)
        }
    }

    @staticmethod
    def obtenir_tarif(cylindree, forfait_km):
        cle_forfait = forfait_km if forfait_km in [100, 200, 300] else "+300"
        return TarifsManager.TARIFS.get(cylindree, {}).get(cle_forfait)

    @staticmethod
    def afficher_grille():
        print("GRILLE DES TARIFS LOCATION")
        for moteur, infos in TarifsManager.TARIFS.items():
            print(f"\nPour un moteur de {moteur} cylindres :")
            for km, prix in infos.items():
                print(f"  -> Forfait {km}km : {prix[0]}€/jour | Supp: {prix[1]}€/km")