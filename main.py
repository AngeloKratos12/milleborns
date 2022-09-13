
from random import shuffle, choice


    
accidentRoute, panneEssence, crevaison, limVitesse, feuRouge = 3, 3, 3, 4, 5
reparation, essence, roueSecours, finLimVitesse, feuVert = 6, 6, 6, 6, 14
asVolant, citerne, increvable, prioritaire = 1, 1, 1, 1
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
            'prioritaire': prioritaire
        }
        
distances = {
            'escargot': escargot,
            'canard': canard,
            'papillon': papillon,
            'lievre': lievre,
            'hirondelle': hirondelle
        }


##Les cartes
cartesList = ['attaques', 'defenses', 'bottes', 'distances']


attaquesList = ['accidentRoute','panneEssence','crevaison','limVitesse','feuRouge']
defensesList = ['reparation','essence','roueSecours','finLimVitesse','feuVert']
bottesList = ['asVolant','citerne','increvable','prioritaire']
distancesList = ['escargot','canard','papillon','lievre','hirondelle']
carte_init = [cartesList ,attaquesList, defensesList, bottesList, distancesList]


def reduction(mycarteType, mycarteChoice):
    
    '''
        UNE FONCTION QUII FAIT DIMINUER LE NOMBRE DE CARTE OBTENUE
    '''
    
    if mycarteType == 'attaques':
        attaques[mycarteChoice] -= 1
        #print(attaques)
        nbrcarte =  attaques[mycarteChoice]
        #print(nbrcarte)
        
    elif mycarteType == 'defenses':
        defenses[mycarteChoice] -= 1
        #print(defenses)
        nbrcarte = defenses[mycarteChoice]
        #print(nbrcarte)
        
    elif mycarteType == 'bottes':
        bottes[mycarteChoice] -= 1 
        #print(bottes)
        nbrcarte = bottes[mycarteChoice]
        #print(nbrcarte)

    elif mycarteType == 'distances':
        distances[mycarteChoice] -= 1
        #print(distances)
        nbrcarte = distances[mycarteChoice]
        #print(nbrcarte)

    return nbrcarte



def partCarte(cartesList, attaquesList,defensesList,bottesList,distancesList):
    
    '''
        function qui distribue les cartes
    '''
    print(cartesList) 
    
            
    shuffle(cartesList)
    mycarteType = choice(cartesList)
    ##
    
    if mycarteType == 'attaques':
        shuffle(attaquesList)
       # print(attaques)
        mycarte =  choice(attaquesList)
        
    elif mycarteType == 'defenses':
        shuffle(defensesList)
       # print(defenses)
        mycarte =  choice(defensesList)
        
    elif mycarteType == 'bottes':
        shuffle(bottesList)
        #print("bottes list: ", bottesList)
        mycarte =  choice(bottesList)

    else:
        shuffle(distancesList)
       # print(distances)
        mycarte =  choice(distancesList)
        
    return (mycarte, mycarteType)
    

def init(player, carte):
    
    cartesList, attaquesList,defensesList,bottesList,distancesList = carte[0],carte[1],carte[2],carte[3],carte[4]
    ##Distribution des cartes
    mycartes = {}  ##Tous mes cartes
    helena_cartes = {}
    
    for i in range(player):
        
        a, de, b, di = len(attaquesList), len(defensesList), len(bottesList), len(distancesList)
        if a!=0 and de!=0 and b!=0 and di!=0 :
            cartesList = cartesList
        
        
        else:
            if a == 0:
                if 'attaques' in cartesList:
                    index = cartesList.index('attaques')
                    cartesList.pop(index)
            
            elif de == 0:
                if 'defenses' in cartesList:
                    index = cartesList.index('defenses')
                    cartesList.pop(index)
            
            
            elif b == 0:
                if 'bottes' in cartesList:
                    index = cartesList.index('bottes')
                    cartesList.pop(index)
            
            else:
                if 'distances' in cartesList:
                    index = cartesList.index('distances')
                    cartesList.pop(index)
            
            
        
        mycarte = partCarte(cartesList, attaquesList,defensesList,bottesList,distancesList)  ##une de mes cartes
        
        mycarteType = mycarte[1]
        mycartechoice = mycarte[0]
        
        
        nbrCarteVerification = reduction(mycarteType, mycartechoice)
        #print(nbrCarteVerification)
        
        
        if nbrCarteVerification == 0:
            
            if mycarteType == 'attaques':
                part = i % 2
                if int(part) == 0:
                    mycartes['carte' + str(i + 1)] = mycartechoice
                
                else:
                    helena_cartes['carte' + str(i + 1)] = mycartechoice
                    
                i = attaquesList.index(mycartechoice)
                attaquesList.pop(i)
                
            
            elif mycarteType == 'defenses':
                part = i % 2
                if int(part) == 0:
                    mycartes['carte' + str(i + 1)] = mycartechoice
                
                else:
                    helena_cartes['carte' + str(i + 1)] = mycartechoice
                    
                i = defensesList.index(mycartechoice)
                defensesList.pop(i)
                
                
            elif mycarteType == 'bottes':
                part = i % 2
                if int(part) == 0:
                    mycartes['carte' + str(i + 1)] = mycartechoice
                
                else:
                    helena_cartes['carte' + str(i + 1)] = mycartechoice
                    
                i = bottesList.index(mycartechoice)
                bottesList.pop(i)
                #print(bottesList)               
                
                
            else:
                part = i % 2
                if int(part) == 0:
                    mycartes['carte' + str(i + 1)] = mycartechoice
                
                else:
                    helena_cartes['carte' + str(i + 1)] = mycartechoice
                    
                i = distancesList.index(mycartechoice)
                distancesList.pop(i)
                
            
            
            #nbrCarteVerification = reduction(mycarteType, mycartechoice)
        else:
            part = i % 2
            if int(part) == 0:
                mycartes['carte' + str(i + 1)] = mycartechoice
            
            else:
                helena_cartes['carte' + str(i + 1)] = mycartechoice
                
            
    print(attaques)
    print(defenses)
    print(bottes)
    print(distances)
    
    return (mycartes,helena_cartes, (cartesList, attaquesList,defensesList,bottesList,distancesList))
    
        
    
if __name__ == '__main__':
    distribution = init(12, carte_init)
    your_carte = distribution[0]
    helena_carte = distribution[1]
    resteCarte = distribution[2]
    print('your carte: ', your_carte)
    print()
    print('helena carte: ', helena_carte)