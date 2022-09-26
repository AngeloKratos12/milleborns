
from random import shuffle, choice


class ManageCarte:
    '''
        une classe pour manager la carte
    '''

    def partCarte(cartesList, attaquesList,defensesList,bottesList,distancesList):
        
        '''
            function qui choisi une carte
        '''
        #print(cartesList) 
        
                
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

    
    
    def mitsabo(mycartes, resteCarte, nbrCarteVerification,mycarteType,mycartechoice):
        cartesList, attaquesList,defensesList,bottesList,distancesList = resteCarte[0],resteCarte[1],resteCarte[2],resteCarte[3],resteCarte[4]
        
        
        if nbrCarteVerification == 0:
            
            if mycarteType == 'attaques':
                mycartes.append(mycartechoice)     
                i = attaquesList.index(mycartechoice)
                attaquesList.pop(i)
                
            
            elif mycarteType == 'defenses':
                mycartes.append(mycartechoice)  
                i = defensesList.index(mycartechoice)
                defensesList.pop(i)
                
                
            elif mycarteType == 'bottes':
                mycartes.append(mycartechoice)     
                i = bottesList.index(mycartechoice)
                bottesList.pop(i)
                #print(bottesList)               
                
                
            else:
                mycartes.append(mycartechoice)     
                i = distancesList.index(mycartechoice)
                distancesList.pop(i)
                
        else:
            mycartes.append(mycartechoice)
        
        resteCarte = (cartesList, attaquesList,defensesList,bottesList,distancesList)
        
        return (mycartes, resteCarte)
            
    
        
   

    

