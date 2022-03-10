import json
import random
from Features.speak import speak
# for intent in intents ['intents']:
#             if tag == "Bye" and intent["tag"] == "Bye":

def quick_reply():
    with open("intents.json", 'r') as json_data:
        intents = json.load(json_data)
        
        for intent in intents['intents']:
            if intent['tag'] == "reply":
               reply =  random.choice(intent["responses"])
               speak(reply)
               
def wish_reply():
    with open("intents.json", 'r') as json_data:
        intents = json.load(json_data)
        
        for intent in intents['intents']:
            if intent['tag'] == "wishme":
               reply =  random.choice(intent["responses"])
               speak(reply)
    
        


