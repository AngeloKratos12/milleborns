##Mille borne 106 cartes

class Carte:
    ##Attaques 18 cartes
    """
        
            3 cartes « Accident de la route »
            3 cartes « Panne d’essence »
            3 cartes « Crevaison »
            4 cartes « Limitation de vitesse »
            5 cartes « Feu rouge »

    """
    def attaques():
        
        attaques = {
            'accidentRoute': 3,
            'panneEssence':3,
            'crevaison': 3,
            'limVitesse': 4,
            'feuRouge': 5
        }


    #Defenses 38 cartes
    """
        6 cartes « Réparations »
        6 cartes « Essence »
        6 cartes « Roue de secours »
        6 cartes « Fin de limitation de vitesse »
        14 cartes « Feu vert »

    """
    def defenses():
        defenses = {
            'reparation': 6,
            'essence': 6,
            'roueSecours': 6,
            'finLimVitesse': 6,
            'feuVert': 14
        }

    #Bottes 4 cartes
    """

        1 carte As du volant
        1 carte Camion-Citerne
        1 carte Increvable
        1 carte Prioritaire

    """

    def bottes():
        bottes = {
            'asVolant': 1,
            'citerne': 1,
            'increvable': 1,
            'prioritaire': 1
        }

    #distance 346 cartes

    """

        10 cartes « 25kms » (escargot)
        10 cartes « 50 kms » (canard)
        10 cartes « 75 kms » (papillon)
        12 cartes « 100 kms » (lièvre)
        4 cartes « 200 kms » (hirondelle)

        
    """

    def distances():
        distances = {
            'escargot': 10,
            'canard': 10,
            'papillon': 10,
            'lievre': 12,
            'hirondelle': 4
        }