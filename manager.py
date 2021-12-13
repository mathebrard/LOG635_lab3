from os import close, kill
import codecs
from crimeEngine import CrimeInference
from aima.logic import *
from random import randint, randrange
import nltk



class Manager:

    def __init__(self,time):
        self.engine = CrimeInference()
        self.usedSentences = []
        self.crimeTime = time
        self.itemsOfInterest = ["le couteau","le revolver","la corde","le tuyau","la matraque","le chandelier"]
        self.peopleOfInterest = ["Mustard","Peacock", "Scarlet", "Plum", "White","Green"]
        self.rooms = ["le salon","la cuisine","le bureau","le studio","la bibliothèque","la cave"]
        self.engine.add_clause('HeureCrime({})'.format(self.crimeTime))
        self.engine.add_clause('UneHeureApresCrime({})'.format(self.crimeTime+1))


    # Cette fonction retourne le format d'une expression logique de premier ordre
    def results_as_string(self,results):
        res = ''
        for result in results:
            # synrep = syntactic representation
            # semrep = semantic representation
            for (synrep, semrep) in result:            
                res += str(semrep)
        return res

    # Cette fonction transforme une phrase en fraçais dans une expression logique du premier ordre
    def to_fol(self,fact, grammar):
        sent = self.results_as_string(nltk.interpret_sents(fact, grammar))
        print(sent)
        return sent   

    def ask_question(self):
        structure = randrange(3)
        itemOfInterest = ""
        
        if structure == 0:
            print("This is structure 0")
            if len(self.itemsOfInterest) == 0:
                self.ask_question()
            else:    
                itemOfInterest = self.itemsOfInterest[randint(0,len(self.itemsOfInterest)-1)]
                sentence = "Où est "+ itemOfInterest +"?"
                question = 'grammars/arme_piece.fcfg'
                self.itemsOfInterest.remove(itemOfInterest)
                if self.checkSentence(sentence):
                    self.writeAnswer(sentence,question)

        elif structure == 1:
            print("This is structure 1")
            if len(self.peopleOfInterest) == 0:
                self.ask_question()
            else:    
                itemOfInterest = self.peopleOfInterest[randint(0,len(self.peopleOfInterest)-1)]
                sentence = "Où était "+ itemOfInterest +" à "+str(self.crimeTime)+"h?"
                question = 'grammars/personne_piece_heure.fcfg'
                self.peopleOfInterest.remove(itemOfInterest)
                if self.checkSentence(sentence):
                    self.writeAnswer(sentence,question)

        elif structure == 2:
            print("This is sctucture 2")
            structure = randrange(2)
            if structure == 0:
                if len(self.itemsOfInterest) == 0:
                    self.ask_question()
                else:
                    itemOfInterest = self.itemsOfInterest[randint(0,len(self.itemsOfInterest)-1)]
                    roomOfInterest = self.rooms[randint(0,len(self.rooms)-1)]
                    sentence = "Est-ce que "+itemOfInterest+" est dans "+roomOfInterest+"?"
                    answer = [itemOfInterest + " est dans " + roomOfInterest]
                    question = 'grammars/arme_piece.fcfg'
                    self.itemsOfInterest.remove(itemOfInterest)
                    if self.checkSentence(sentence):
                        self.writeYesNoAnswer(sentence,answer,question)

            elif structure == 1:
                if len(self.peopleOfInterest) == 0:
                    self.ask_question()
                else:
                    itemOfInterest = self.peopleOfInterest[randint(0,len(self.peopleOfInterest)-1)]
                    roomOfInterest = self.rooms[randint(0,len(self.rooms)-1)]
                    sentence = "Est-ce que "+itemOfInterest+" était dans "+roomOfInterest+" à "+str(self.crimeTime)+"h?"
                    answer = [itemOfInterest + " était dans " + roomOfInterest + " à "+str(self.crimeTime)+"h"]
                    question = 'grammars/personne_piece_heure.fcfg'
                    self.peopleOfInterest.remove(itemOfInterest)
                    if self.checkSentence(sentence):
                        self.writeYesNoAnswer(sentence,answer,question)

    def checkSentence(self,sentence):
        for item in self.usedSentences:
            if(sentence == item):
                print("the question has already been asked")
                self.ask_question()
                return False
        self.usedSentences.append(sentence)
        return True

    def writeAnswer(self,sentence,structure):
        print(sentence)
        input("Press any key to read answer.txt")
        with codecs.open('answer.txt','r','utf8') as f:
            lines = f.readlines()
            if len(lines) > 1 or lines[0].endswith("\n"):
                print("s'il vous plait écrire seulement sur une ligne")
                self.writeAnswer(sentence,structure)
            answer = [lines[0]]
            self.engine.add_clause(self.to_fol(answer, structure))
    
    def writeYesNoAnswer(self,sentence, answer, structure):
        print(sentence)
        input("Press any key to read answer.txt")
        with codecs.open('answer.txt','r','utf8') as f:
            lines = f.readlines()
            if len(lines) > 1 or lines[0].endswith("\n"):
                print("s'il vous plait écrire seulement sur une ligne")
                self.writeYesNoAnswer(sentence,answer,structure)
            sheetAnswer = [lines[0]]
            print(sheetAnswer)
            if (sheetAnswer[0] == "Oui" or sheetAnswer[0] == "oui"):
                self.engine.add_clause(self.to_fol(answer, structure))
            elif (sheetAnswer[0] == "Non" or sheetAnswer[0] == "non"):
                print("The statement is false") 
            else:
                print("s'il vous plait écrire seulement oui ou non")
                self.writeYesNoAnswer(sentence,answer,structure)  

    def receiveData(self, itemOfInterest, placeOfInterest, time = None):
        if time == None:
            time = self.crimeTime+1
        if itemOfInterest in self.itemsOfInterest:
            answer = [itemOfInterest +" est dans "+placeOfInterest]
            grammar = 'grammars/arme_piece.fcfg'
            self.itemsOfInterest.remove(itemOfInterest)
            for items in self.itemsOfInterest:
                print(items)
            self.engine.add_clause(self.to_fol(answer,grammar))
        else:
            answer = [itemOfInterest + " était dans " + placeOfInterest + " à "+str(time)+"h"]
            grammar = 'grammars/personne_piece_heure.fcfg'
            self.engine.add_clause(self.to_fol(answer,grammar))
        return
    
    def addVictim(self, victim):
        peopleArray = self.peopleOfInterest
        self.engine.add_clause(self.to_fol([victim+" est mort"],'grammars/personne_morte.fcfg'))
        for person in peopleArray:
            if person != victim:
                self.engine.add_clause(self.to_fol([person+" est vivant"],'grammars/personne_vivant.fcfg'))

    def solveCrime(self):
        killer = self.engine.get_suspect()
        weapon = self.engine.get_crime_weapon()

        while((str(killer)=="False") | (str(weapon)=="False")):
            self.ask_question()
            killer = self.engine.get_suspect()
            weapon = self.engine.get_crime_weapon()
        sentence = (str(killer) +" a tué "+str(self.engine.get_victim())+ " avec "+str(weapon) +" dans "+ str(self.engine.get_crime_room()))
        return sentence

manager = Manager(2) 


#for x in range(3):
#    manager.receiveData("le couteau","la cave")


#manager.addVictim("White")


#manager.receiveData("White","la bibliothèque")
#manager.receiveData("le revolver", "la bibliothèque")
#manager.receiveData("le chandelier","le salon")
#manager.receiveData("Green","le salon")

for x in range(15):
    manager.ask_question()
#manager.receiveData("la corde","le salon")

manager.addVictim("White")
manager.receiveData("White","le salon",2)
manager.receiveData("White","le salon",3)


crime = manager.solveCrime()
print(crime)

print(manager.engine.get_victim())
print(manager.engine.get_crime_room())
print(manager.engine.get_suspect())
print(manager.engine.get_innocent())
print(manager.engine.get_crime_weapon())
print(manager.engine.get_crime_hour())
print(manager.engine.get_crime_hour_plus_one())