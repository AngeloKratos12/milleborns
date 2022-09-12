
from random import shuffle, choice


    
accidentRoute, panneEssence, crevaison, limVitesse, feuRouge = 3, 3, 3, 4, 5
reparation, essence, roueSecours, finLimVitesse, feuVert = 6, 6, 6, 6, 14
asVolant, citerne, increvable, priioritaire = 1, 1, 1, 1
escargot, canard, papillon, lievre, hirondelle = 10, 10, 10, 12, 4



attaques = {
            'accidentRoute': accidentRoute,
            'panneEssence':panneEssence,
            'crevaison': crevaison,
            'limVitesse': limVitesse,
            'feuRouge': feuRouge
        }


defenses = {
            'reparation': reparation,
            'essence': essence,
            'roueSecours': roueSecours,
            'finLimVitesse': finLimVitesse,
            'feuVert': feuVert
        }
    
    
bottes = {
            'asVolant': asVolant,
            'citerne': citerne,
            'increvable': increvable,
            'prioritaire': priioritaire
        }
        
distances = {
            'escargot': escargot,
            'canard': canard,
            'papillon': papillon,
            'lievre': lievre,
            'hirondelle': hirondelle
        }


def reduction(mycarteType, mycarteChoice):
    
    '''
        UNE FONCTION QUII FAIT DIMINUER LE NOMBRE DE CARTE OBTENUE
    '''
    
    if mycarteType == 'attaques':
        attaques[mycarteChoice] -= 1
        nbrcarte =  attaques[mycarteChoice]
        print(nbrcarte)
        
    elif mycarteType == 'defenses':
        defenses[mycarteChoice] -= 1
        nbrcarte = defenses[mycarteChoice]
        print(nbrcarte)
        
    elif mycarteType == 'defenses':
        bottes[mycarteChoice] -= 1 
        nbrcarte = bottes[mycarteChoice]
        print(nbrcarte)

    elif mycarteType == 'defenses':
        distances[mycarteChoice] -= 1
        nbrcarte = distances[mycarteChoice]
        print(nbrcarte)

    return 



def partCarte():
    
    '''
        function qui distribue les cartes
    '''
     ##Les cartes
    cartes = ['attaques', 'defenses', 'bottes', 'distances']


    attaques = ['accidentRoute','panneEssence','crevaison','limVitesse','feuRouge']
    defenses = ['reparation','essence','roueSecours','finLimVitesse','feuVert']
    bottes = ['asVolant','citerne','increvable','prioritaire']
    distances = ['escargot','canard','papillon','lievre','hirondelle']
    
    ##melanger les cartes
    shuffle(cartes)
    
    mycarteType = choice(cartes)
    
    ##
    if mycarteType == 'attaques':
        shuffle(attaques)
       # print(attaques)
        mycarte =  choice(attaques)
        
    elif mycarteType == 'defenses':
        shuffle(defenses)
       # print(defenses)
        mycarte =  choice(defenses)
        
    elif mycarteType == 'bottes':
        shuffle(bottes)
        #print(bottes)
        mycarte =  choice(bottes)

    else:
        shuffle(distances)
       # print(distances)
        mycarte =  choice(distances)
        
    return (mycarte, mycarteType)
    

def init():
    
    ##Distribution des cartes
    mycartes = {}  ##Tous mes cartes
    for i in range(6):
        mycarte = partCarte()  ##une de mes cartes
        mycarteType = mycarte[1]
        mycartechoice = mycarte[0]
        nbrCarteVerification = reduction(mycarteType, mycartechoice)
        if nbrCarteVerification != -1:
            verified = True
        else:
            verified = False
        
        #while verified == False:
            
        print(mycarte)
        
        
    print(mycartes)
    
        
   


if __name__ == '__main__':
    init()