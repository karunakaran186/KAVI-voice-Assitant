
text = """Abdul Rashid Salim Salman Khan (Hindi: [səlˈmɑːn xɑːn]; 27 December 1965)[4] is an Indian actor, film producer, singer, painter[5] and television personality who works in Hindi films. In a film career spanning over thirty years, Khan has received numerous awards, including two National Film Awards as a film producer, and two Filmfare Awards for acting.[6] He is cited in the media as one of the most commercially successful actors of Indian cinema.[7][8] Forbes included him in their 2015 list of Top-Paid 100 Celebrity Entertainers in the world; Khan tied with Amitabh Bachchan for No. 71 on the list, both with earnings of $33.5 million.[9][10] According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was the highest-ranked Indian with 82nd rank with earnings of $37.7 million.[11][12] He is also known as the host of the reality show, Bigg Boss since 2010.[13]

The eldest son of screenwriter Salim Khan, Khan began his acting career with a supporting role in Biwi Ho To Aisi (1988), followed by a leading role in Maine Pyar Kiya (1989). Khan continued in Bollywood in the 1990s with roles in several productions, including the romantic drama Hum Aapke Hain Koun..! (1994), the action comedy Andaz Apna Apna (1994), the action thriller Karan Arjun (1995), the comedy Biwi No.1 (1999), and the family drama Hum Saath-Saath Hain (1999). After a brief period of decline in the 2000s, Khan achieved greater stardom in the 2010s by playing the lead role in successful action films like Dabangg (2010), Ready (2011), Ek Tha Tiger (2012), Kick (2014), Sultan (2016) and Tiger Zinda Hai (2017).

In addition to his acting career, Khan is a television presenter and promotes humanitarian causes through his charity, Being Human Foundation.[14] Khan's off-screen life is marred by controversy and legal troubles. In 2015 he was convicted of culpable homicide for a negligent driving case in which he ran over five people with his car, killing one, but his conviction was set aside on appeal.[15][16][17][18] On 5 April 2018, Khan was convicted in a blackbuck poaching case and sentenced to five years imprisonment.[19][20] He is currently out on bail while an appeal is being heard.[21]

Salman Khan has starred in ten of the highest grossers of the year, starting from 1947 to 2020, which is highest for any actor in history of Hindi cinema.[22]
"""

import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from text_preprocessing import bag_of_words, bag_of_words_2, lemmatize
from text_preprocessing import lemmatize, bag_of_words_2, bag_of_words, Tf_Idf
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
cv = CountVectorizer()
tf_idf = TfidfVectorizer()
corpus =[]
def bag_of_words_2(tokenized_sentence):
    """
    Packing all those descrete packed words into some model understandable and sending forward
    
    There is one diadvantage of bag of words though,
    it assigns the same wietage to all the words
    to solve this problem we have another system called
    word2vec or TFIDF
    (term frequency–inverse document frequency)
    """
    sentence_word = [lemmatize(word) for word in tokenized_sentence if not word in set(stopwords.words('english')) ]
    bag = cv.fit_transform(sentence_word).toarray()
    return bag
"""
TFIDF-  (term frequency–inverse document frequency)
term Frequency =( no of words in sentence )/no of words in sentence
inverse document frequency==
                          log((no of sentences)/(no of sentences containing words))
________________________
                         |
#Finally = TF*IDF        |
_________________________|
"""
def Tf_Idf(tokenized_sentence):
    sentence_word = [lemmatize(word) for word in tokenized_sentence if not word in set(stopwords.words('english')) ]
    bag = tf_idf.fit_transform(sentence_word)
    return bag

sentences = sent_tokenize(text)
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

words = ["'m", "'s", 'Bad', 'Entertain', 'I', 'Thank', 'What', 'alarm', 'amuse', 'angry', 'assistant', 'atmosphere', 'bbye', 'best', 'better', 'bored', 'buddy', 'bulletin', 'bye', 'ca', 'capture', 'carry', 'check', 'competitor', 'cool', 'could', 'current', 'date', 'day', 'describe', 'din', 'eager', 'easy', 'eeji', 'enemy', 'enough', 'everything', 'excited', 'exit', 'fantastic', 'feeling', 'find', 'fine', 'friend', 'frustrated', 'gang', 'gather', 'get', 'go', 'going', 'good', 'google', 'headline', 'heat', 'hello', 'hemlo', 'hey', 'hii', 'hilight', 'hola', 'hold', 'hour', 'ill', 'info', 'inform', 'information', 'irritated', 'jarvis', 'joke', 'know', 'later', 'laugh', 'let', 'listen', 'little', 'location', 'make', 'map', 'mindblowing', 'minute', 'mood', 'music', "n't", 'name', 'need', 'news', 'nice', 'noice', 'nothing', 'nuke', 'ok', 'okay', 'okeah', 'panic', 'party', 'pause', 'picnic', 'play', 'playing', 'please', 'quit', 'relative', 'relaxed', 'repeat', 'reportage', 'rest', 'right', 's', 'sad', 'say', 'screen']


# print("_______bag of words_2")
# print( bag_of_words_2(corpus))
# print("________bag of words__")
# print(bag_of_words(corpus,corpus ))
# print("_______Tf_Idf_______")
# print(Tf_Idf(corpus,words))
#_____________________practice session_____-

# print("____________practice session__________")
# l1 = [1,2,3,4,5,6]

# l2 = l1.append(4)
# print("________l2______")
# print(l2)
# print("________l1______")
# print(l1)

# l3 = l1.extend([1,2,4323,24,6437,54])
# print("________l3______")
# print(l3)
# print("________l1______")
# print(l1)
