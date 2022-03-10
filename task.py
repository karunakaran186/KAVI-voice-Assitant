#2 types of function
# 1 - Non input
#eg: time, date,speedtest

# 2 - Input
# google search, wikipedia

#First we will have to create functions and then add them to the json file
import random
from Features.news import get_news,more_news,getNewsUrl
import datetime
from Features.listen import listen
from Features.speak import speak
import wikipedia
import json
from Features.wolfram import wolfram_ssl
try:
    with open('intents.json', 'r') as f:
        intents = json.load(f) #Naming the loaded json file as intents which actually is a dictionary 
except Exception as e:
    print(e)
try:
    import pywhatkit
except Exception as e:       #it requires internet connection
    print(e)
from Features import joke
from Features.alarm import  set_alarm
from Features.weather import  weather, weather_updates , Location
import os
import csv

def Time():
    time = datetime.datetime.now().strftime("%H: %M")
    speak(time)
def Date():
    date = datetime.date.today()
    speak(date)
def Day():
    day = datetime.datetime.now().strftime("%A")
    speak(day) 
def NEWS():
     
#    speak('Source: The Times Of India')
    try:
        responses = ["news","Headlines are ","Top 5 bulletins are ", 'Todays Headlines are..']
        speak(random.choice(responses))
        speak(get_news())
        speak("Do you want to listen more news ?")
        ans = listen()
        #for intent in intents ['intents']:
        if ans == "yes" : #and intent["tag"] == "Positive:
            news_res = more_news()
            for index, articles in enumerate(news_res):
                print(articles['title'])
                speak(articles['title'])
                if index == len(news_res)-2:
                        break
        speak('These were the top headlines, Have a nice day Sir!!..')
        #speak("For your convenience, I am printing it on the screen sir.")
        #print(*get_news(),end="\n")
    except:
        speak("Please connect to the internet")
    
def read_prev_response():
    lis = list(csv.reader(open('data.csv')))
    l = lis[-1]
    prev_response = str(l[-1])
    speak(prev_response)
    return prev_response



def final_weather():
    weather()
    speak("Do you want to listen more in detail?")
    ans = listen()
    if ans == "yes":
        weather_updates() 
# def wait(amt=10):
    # speak("how many minutes you want me to wait?")
    # # speak("30 seconds", "1 minute", "2 minutes" or "5 minutes")
    # amt = float(listen().replace("minutes", "").replace("minute", ""))
    # speak(f"ok i'll wait for {amt} minutes")
    # time.sleep(amt*60)
    # speak("ok, listening now...")
    

    
    
    
def location(query):
    said = query.split(" ")
    location = said[1] #obtain place name
    speak("Hold on, I will show you where {location} is")
    os.system("google-chrome https://www.google.nl/maps/place/" + location)
    speak("Here it is....")

def InputExecution(tag, query):
    if "wikipedia" in  tag:
        try:
            result = wikipedia.summary(query, sentences = 3)
            speak(result) 
        except Exception as e:
            print("Exception: ", e)
            query = str(query).replace("google", "").replace("search", "").replace("","").replace("what is","").replace("search about","").replace("search for","").replace("find","")
            try:
                pywhatkit.search(query)
            except Exception as e:
                print("Exception: ", e)
                speak("Please connect to the internet")
    elif "google" in tag:
        query = str(query).replace("google", "").replace("search", "").replace("","").replace("what is","").replace("search about","").replace("search for","").replace("find","")
        try:
            pywhatkit.search(query)
        except Exception as e:
            print("Exception: ", e)
            speak("Please connect to the internet")
    elif "weather" in tag :
        try:
            final_weather()
        except Exception as e:
            print("Exception: ", e)
            speak("Couldn't connect to the internet")
    elif 'play' in tag:
        song = query.replace('play', '')
        speak("ok,playing" + song)
        try:
            pywhatkit.playonyt(song)  
        except Exception as e:
            print("Exception: ", e)
            speak("I'm having trouble understanding right now")
      
    
def NoninputExecution(query):
    query = str(query)
    
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
    elif "news" in query:
        try:
            NEWS()
        except Exception as e:
            print("Exception: ",e)
            speak("Couldn't connect to the internet")
            
    elif "joke" in query:
        joke.startJoke()
    elif "repeat" in query:
        read_prev_response()
    elif "alarm" in query:
        set_alarm()
    elif "loaction" in query:
        try:
            Location()
        except Exception as e:
            print("Exception: ",e)
            speak("Couldn't connect to the internet")
            
    elif "bye" in query :
        speak
        exit(0)
    else:
        try:
            wolfram_ssl()
        except Exception as e:
            print("Exception: ",e)
            speak("Please connect to the internet")
        
    


# read_prev_response()

# Day()
