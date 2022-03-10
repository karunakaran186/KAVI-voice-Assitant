
import nltk
from nltk.corpus import words
from nltk.metrics.distance import (
    edit_distance,
    jaccard_distance,
    )
from nltk.util import ngrams
nltk.download('words')
import pandas
correct_spellings = words.words()
spellings_series = pandas.Series(correct_spellings)
spellings_series
def jaccard(entries, gram_number):
    
    outcomes = []
    for entry in entries: #iteratively for loop
        spellings = spellings_series[spellings_series.str.startswith(entry[0])] 
        distances = ((jaccard_distance(set(ngrams(entry, gram_number)),
                                       set(ngrams(word, gram_number))), word)
                     for word in spellings)
        closest = min(distances)
        outcomes.append(closest[1])
    return outcomes
def JDreco(entries=["alone musk"]):
    """finds the closest word based on jaccard distance"""
    return jaccard(entries, 3)
print(JDreco())
def editreco(entries=["elone muskk"]):

    outcomes = []
    for entry in entries:
        distances = ((edit_distance(entry,
                                    word), word)
                     for word in correct_spellings)
        closest = min(distances)
        outcomes.append(closest[1])
    return outcomes


print(editreco())