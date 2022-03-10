
# import spacy 
# import numpy as np 
# from spacy.vocab import Vocab 
# nlp = spacy.load('en_core_web_md') 
# new_word = 'bucrest'
# print('Before custom setting') 
# print(Vocab.get_vector('bucrest')) 
# custom_vector = np.random.uniform(-1, 1, (300, )) 
# Vocab.set_vector(new_word, custom_vector) 
# print('After custom setting') 
# print(Vocab.get_vector('bucrest')) 

# Printing the following attributes of each token.
        # text: the word string, has_vector: if it contains
        # a vector representation in the model, 
        # vector_norm: the algebraic norm of the vector,
        # is_oov: if the word is out of vocabulary.
# nlp = spacy.load('en_core_web_md')
# print("Enter two space-separated words")
# words = input()
# tokens = nlp(words)
# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)
# token1, token2 = tokens[0], tokens[1]
# print("Similarity:", token1.similarity(token2))
import spacy
from nltk.corpus import wordnet
import warnings
warnings.filterwarnings("ignore")

nlp = spacy.load('en_core_web_md')
def Get_Synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return set(synonyms)

def Get_Similarities(word):
    similarities = []
    string = f"{word} "
    words = Get_Synonyms(word)
    string_1 = " ".join(word for word in words)
    string = string + string_1
    tokens = nlp(string)
    for i in range(1,len(tokens)):
        token = tokens[i]
        original_word = tokens[0]
        similarity = original_word.similarity((token))
        if similarity >= 0.5:
            similarities.append(str(token))
    # final_string = " ".join(similarities)  
    return similarities
 