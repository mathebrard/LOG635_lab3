from crimeEngine import CrimeInference
from aima.logic import *
import nltk

engine = CrimeInference()


# Cette fonction retourne le format d'une expression logique de premier ordre
def results_as_string(results):
    res = ''
    for result in results:
        # synrep = syntactic representation
        # semrep = semantic representation
        for (synrep, semrep) in result:            
            res += str(semrep)
    return res

# Cette fonction transforme une phrase en fraçais dans une expression logique du premier ordre
def to_fol(fact, grammar):
    sent = results_as_string(nltk.interpret_sents(fact, grammar))
    print(sent)
    return sent   

fact = ['Le revolver est dans la bibliothèque']
engine.add_clause(to_fol(fact, 'grammars/arme_piece.fcfg'))

fact = ['Green est mort à 5h']
engine.add_clause(to_fol(fact,'grammars/personne_morte_heure.fcfg'))

fact = ['Green est mort']
engine.add_clause(to_fol(fact,'grammars/personne_morte.fcfg'))

fact = ['White était dans la bibliothèque à 5h']
engine.add_clause(to_fol(fact,'grammars/personne_piece_heure.fcfg'))
