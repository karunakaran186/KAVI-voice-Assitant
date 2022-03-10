# importing modules
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import json
from Neural_Network.text_preprocessing import ignore_words,preprocessing
from tensorflow.keras.models import save_model
from similar_words import Get_Similarities
import warnings
warnings.filterwarnings("ignore")
try:
    with open('intents.json', 'r') as f:
        intents = json.load(f) #Naming the loaded json file as intents which actually is a dictionary 
except Exception as e:
    print(e)

all_patterns = [] 
tags = [] 
tag_per_sentence = [] 
# trained_words = []

for intent in intents['intents']: 
     tag = intent['tag']
     tags.append((tag))     
     for pattern in intent['patterns']:
        processed_pattern = preprocessing(pattern)
        similar_words = Get_Similarities(processed_pattern)
        similar_words = [word for word in similar_words if word not in all_patterns]
        tag_words = [f"{processed_pattern}"]
        # similar_words = similar_words.split()
        # for i in similar_words:
         # all_patterns.append((str(i).lower() ))
        tag_words.extend(similar_words)    
        for pattern in set(tag_words): 
            tag_per_sentence.append((preprocessing(pattern), tag))
            
tag_per_sentence = set(tag_per_sentence)
with open("tag_per_sent.text", "w") as f:
    f.write(str(tag_per_sentence))   
data = pd.DataFrame(tag_per_sentence,columns =['Patterns','tags'])
data = data.dropna()

# Here, ngram_range specifies how to transform the data, ngram_range of (1, 2) will have both monograms and bigrams in the Tf-Idf vectors. stop_words specifies the language from which the stop words to be removed.




if __name__ == '__main__':
    vectorizer  = TfidfVectorizer(ngram_range=(1,2), stop_words=ignore_words)
    training_data_tfidf = vectorizer.fit_transform(data['Patterns']).toarray()
    #One - hot encoding
    le = LabelEncoder()
    training_data_tags_le = pd.DataFrame({"tags": le.fit_transform(data['tags'])})
    training_data_tags_dummy_encoded = pd.get_dummies(training_data_tags_le["tags"]).to_numpy()
    print(len(training_data_tfidf[0]))
    chatbot = Sequential()
    chatbot.add(Dense(32, input_shape=(len(training_data_tfidf[0]),)))
    chatbot.add(Dense(64))
    chatbot.add(Dense(64))
    chatbot.add(Dense(64))
    chatbot.add(Dense(len(training_data_tags_dummy_encoded[0]), activation="softmax"))
    print(len(training_data_tags_dummy_encoded[0]))
    chatbot.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    # fitting DNN
    chatbot.fit(training_data_tfidf, training_data_tags_dummy_encoded, epochs=200, batch_size=512)
    
    print(chatbot.summary())
    # saving model file
    save_model(chatbot, "TrainData")

    