# Importing Modules for Basic Functionality:
import os
import time
import subprocess
import datetime
import requests
from email.mime import audio
from numpy import place
from setuptools import Command

# For Speech Recognition
import speech_recognition as sr

# Importing Additional Modules for extra functionality
import pyttsx3
import pywhatkit
import pyjokes
from PIL import Image
import wikipedia
import webbrowser
import wolframalpha
import psutil

# Setting up all the necessary Configs for the bot
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',170)     
engine.setProperty('volume',0.7)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
client=wolframalpha.Client('33Y4Y4-AQE2783RKY')

# Sub Functions Starts here
# This function will fetch Images
def img_requests(txt):   
    response=requests.get("https://source.unsplash.com/random{0}".format(txt))
    file=open('container.jpg','wb')
    file.write(response.content)
    img=Image.open(r"container.jpg")
    img.show()
    file.close

# This function will talk back
def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    
# This function will initiate the starting of the bot    
def wishMe():     
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")
    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   
    else:
       talk("Good Evening!")      
    talk("I am kavi, I am a Virtual Assistant, I am here to help you")
    engine.setProperty('rate',185)

# This Function will take the voice input from the user
def take_command():    
    r = sr.Recognizer()     
    with sr.Microphone() as source:
        time.sleep(1)
        talk("Listening")
        r.pause_threshold=0.8                 
        r.energy_threshold=250                 
        audio = r.listen(source)      
        try:            
            command = r.recognize_google(audio)            
            print(f"{command}\n")
            return command
        except Exception as e:            
            print("Pardon me,Please say that again")
            return "Not Found"
                    
# This function will fetch the overall performance of the computer
def get_memory_consumption():
    pid = os.getpid()
    py = psutil.Process(pid)
    memory_use = py.memory_info()[0] / 2. ** 30
    return memory_use
# This enable's the one time wishing 
hi = 0
if hi == 0:
    wishMe()
else:
    hi+=1
    print('listening')
if __name__=='__main__':
    while True:
        command = take_command().lower()
        if "exit" in command or "stop" in command or "shutdown" in command:
            talk("Your AI assistant kavi is shutting down,Good bye and have a good day (:")
            break
        elif 'temperature' in command:
             talk("Please tell me the location !")
             location=take_command()
             query2="weather forecast of {}".format(location)
             try:   
                res = client.query(query2)
                output=next(res.results).text
                talk("the temperature of the day will be "+output)
             except Exception as e:
                print("Sorry Please try again")
        elif 'images' in command:
            talk("Here are some options you can select from, please provide an number corresponding to your preferred option")                       
            print("""Please provide an option for Image
        # 1, HD Random Picture
        # 2, FHD Random Picture
        # 3, 2K Random Picture
        # 4, 4k Random Picture
        # 5, Picture with User Provided Keywords """)
            ans=input("Enter the number")           
            talk("Please wait while we fetch the images from our database.")
            if 'one' in ans or '1' in ans or 'won' in ans:
                img_requests('/1280x720')
            elif 'two' in ans or '2' in ans or 'tu' in ans:            
                img_requests('/1920x1080')
            elif 'three' in ans or '3' in ans or 'tree' in ans or 'free' in ans:
                img_requests('/2048x1080')
            elif 'four' in ans or '4' in ans or 'food' in ans or 'for' in ans:
                img_requests('/4096x2160')
            elif 'five' in ans or '5' in ans or'fibe' in ans:
                talk("talk keywords seperated by commas ")
                st=take_command()
                if 'comma' in st:
                    st.replace('comma',',')
                st="?"+st
                img_requests(st)
            else:
                talk("Please provide a valid Input")       
        elif 'play' in command:
            talk('playing')
            print('playing')
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'whatsapp' in command:
            phno=input()
            pywhatkit.sendwhatmsg("+91 {}".format(phno), "Please wait while we send the message",
                                  13, 58)
            print("Successfully Sent!")
            continue
        elif 'who is' in command:
            person = command.replace('who is', '')
            source = wikipedia.summary(person, 100)
            print(source)
            talk(source)
        elif 'integrate' or 'differentiate' or 'divide' or 'multiply' or 'add' or 'subtract' in command:
            res = client.query(command)
            try:
                output=next(res.results).text
                talk(output)
            except Exception as e:
                talk("Please provide a valid input")
        elif 'search' in command:
            info = command.replace('search', '')
            general = wikipedia.search(info, 100)
            talk(general)
        elif 'history' in command:
            gen = command.replace('history, battle, movie review', '')
            small = wikipedia.summary(gen, 100)
            talk(small)
        elif 'movie review' in command:
            movie = command.replace('movie review', '')
            small = wikipedia.summary(movie, 10)
            talk(small)
        elif 'are you single' in command:
            talk('no......um.i am in relationship with wireless devices')
        elif 'do you like me' in command:
            talk('yes boss definitely')
        elif 'what is your name' in command:
            talk('My developer karunakran has named me kkavi')
        elif 'cringe' in command:
            talk('alright........he/she was funniest perosn')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        elif 'i am tired' in command:
            talk('you should take a break')
        elif 'favorite game' in command:
            talk('my favorite game is chess')
        elif 'can you dance' in command:
            talk('I cant dance as of now, but I can play some dance music')
        elif 'how do i look' in command:
            talk('juding from your voice, amazing')
        elif 'can you cook' in command:
            talk('i can cook you up amazing bedtime stories if you want')
        elif 'who is your friend' in command:
            talk('her name is nilla voice assistant, she was in another repository')
        elif "where is" in command:
            command = command.replace("where is", "")
            location = command
            talk("User asked to Locate")
            talk(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")     
        elif 'open calculator' in command:
            talk('opening calculator')
            subprocess.call('calc.exe')
        elif 'open word document' in command:
            talk('Opening Word document')
            os.startfile(r'WINWORD.EXE')
        elif 'open notepad' in command:
            talk('Open Notepad')
            os.startfile(r'NOTEPAD.EXE')
        elif "weather" in command:
            api_key = "51d5d78391e312e72cde67174f38e770"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            talk("which city are you looking to know")
            place = take_command()
            complete_url = base_url + "appid=" + api_key + "&q=" + place
            result = requests.get(complete_url)
            x = result.json()
            if x["cod"] != "404":
                y = x["main"]
                city_temperature = y["temp"]
                city_humidiy = y["humidity"]
                ans = x["weather"]
                weather_description = ans[0]["description"]
                talk("Temperature" + str(place) + "in kelvin unit is " +
                     str(city_temperature) +
                     "\n humidity in percentage is " +
                     str(city_humidiy) +
                     "\n description  " +
                     str(weather_description))
                print(str(place) + " Temperature in kelvin unit = " +
                      str(city_temperature) +
                      "\n humidity (in percentage) = " +
                      str(city_humidiy) +
                      "\n description = " +
                      str(weather_description))
        elif "health of kavi" in command:            
            memory = get_memory_consumption()
            talk("I use {0:.2f} GB..".format(memory))
        else:
            talk("Sorry I did not get that")
            

