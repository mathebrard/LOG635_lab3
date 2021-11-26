from os import close
import codecs
from crimeEngine import CrimeInference
from aima.logic import *
from random import randint, randrange
import nltk

engine = CrimeInference()

class Manager:

    def __init__(self):
        print("new manager who this")
        self.usedSentences = []
        self.crimeTime = 2


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
        sent = manager.results_as_string(nltk.interpret_sents(fact, grammar))
        print(sent)
        return sent   

    def ask_question(self):
        itemsOfInterest = ["le couteau","le revolver","la corde","le tuyau","la matraque","le chandelier"]
        peopleOfInterest = ["Mustard","Peacock", "Scarlet", "Plum", "White","Green"]
        rooms = ["le salon","la cuisine","le bureau","le studio","la bibliothèque","la cave"]
        structure = randrange(3)
        
        if structure == 0:
            print("This is structure 0")
            sentence = "Où était "+ itemsOfInterest[randint(0,5)]+" à "+str(self.crimeTime)+"h?"
            if self.checkSentence(sentence):
                self.writeAnswer(sentence)

        elif structure == 1:
            print("This is structure 1")
            sentence = "Où était "+ peopleOfInterest[randint(0,5)]+" à "+str(self.crimeTime)+"h?"
            if self.checkSentence(sentence):
                self.writeAnswer(sentence)

        elif structure == 2:
            print("This is sctucture 2")
            itemsOfInterest=itemsOfInterest+peopleOfInterest
            sentence = "Est-ce que "+itemsOfInterest[randint(0,11)]+" était dans "+rooms[randint(0,5)]+" à "+str(self.crimeTime)+"h?"
            if self.checkSentence(sentence):
                self.writeAnswer(sentence)

    def checkSentence(self,sentence):
        for item in self.usedSentences:
            if(sentence == item):
                print("the question has already been asked")
                self.ask_question()
                return False
        self.usedSentences.append(sentence)
        return True

    def writeAnswer(self,sentence):
        print(sentence)
        input("Press any key to read answer.txt")
        with codecs.open('answer.txt','r','utf8') as f:
            lines = f.readlines()
            if len(lines) > 1 or lines[0].endswith("\n"):
                print("s'il vous plait écrire seulement sur une ligne")
                self.writeAnswer(sentence)
            answer = [lines[0]]
            
            self.to_fol(answer, 'grammars/arme_piece.fcfg')




manager = Manager() 

for x in range(3):
    manager.ask_question()


        

