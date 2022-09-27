
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
            
    
        

class Montour:
    '''
        Une classe qui organise le déroulement du jeu!!
    '''
    
    def face(mycartes, carte, piege,distances, bottes, mypiege):
        distance = ['escargot', 'canard', 'papillon', 'lievre', 'hirondelle']
        botte = ['asVolant','citerne','increvable','prioritaire']
        index = mycartes.index(carte)
        mycartes.pop(index)
        
        if carte in distance:
            
            if piege == False:
                if carte == 'escargot':
                    distances += 25
                
                elif carte == 'canard':
                    distances += 50
                
                elif carte == 'papillon':
                    distances += 75
                
                elif carte == 'lievre':
                    distances += 100
                    
                else:
                    distances += 200
            
            else:
                print('Vous avez encore piegé! Enlevez le piege.')
                piege = True
                while piege == True:
                    mandefa = str(input("Votre tour de poser une carte: "))
                    if carte in distances:
                        piege = True
                        
                    else:
                        piege = False
        
        elif carte in botte:
            bottes.append[carte]
            carte = ManageCarte.mitsabo(mycartes,restecarte,nbrCarteVerification,mycart)
          
            
                
                
            
            
        
        
        
        
        
    

