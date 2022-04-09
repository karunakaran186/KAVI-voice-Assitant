# importing the libraries 
import os
import subprocess
from PIL import Image
import wikipedia
import pywhatkit
import pyttsx3
import speech_recognition as sr
import webbrowser
import requests
import psutil
import datetime
import random
import time
import pygame
from pygame import mixer



# setting the engine properties like voice and volume
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
listener = sr.Recognizer()
mixer.init()

def take_command():
    '''
    This function takes users's voice command and recognizes them.
    '''

    r = sr.Recognizer()
    # try taking in command
    while True: 
        with sr.Microphone() as source:
            print("Listening...")
            talk("listening.....")
            audio = r.record(source, duration=3)

            try:
                command = r.recognize_google(audio, language='en-in')
                print(f"user said:{command}\n")
                return command

            except Exception as e:
                # ask user to repeat if there was some error getting/recognizing it clearly 
                talk("Pardon me,Please say that again")
                print("Pardon me,Please say that again")    
    return 




def talk(text=None, ques=None):

    '''

    This function will give voice output to the user(Fun QnA with Kavi).

    '''

    if text==None:
        # simple talk responses (input => ques)
        if(ques!=None):  
            # talk to kavi like a buddy :)
            if 'are you single' in ques :
                engine.say('I am in relationship with wireless devices')
            elif 'do you like me' in ques:
                engine.say('yes boss definitely')
            elif 'what is your name' in ques:
                engine.say('My devloper karunakran has named me kkavi')
            elif 'cringe' in ques:
                engine.say('alright........he/she was funniest person')
            elif 'joke' in ques:
                joke = get_joke()
                print(joke)
                engine.say(joke)        
            elif 'i am tired' in ques:
                engine.say('you should take a break')
            elif 'favorite game' in ques:
                engine.say('my favorite game is chess')
            elif 'can you dance' in ques:
                engine.say('I cant dance as of now, but I can play some dance music')
            elif 'how do i look' in ques:
                engine.say('juding from your voice, amazing')
            elif 'can you cook' in ques:
                engine.say('i can cook you up amazing bedtime stories if you want')
            elif 'who is your friend' in ques:
                engine.say('her name is nilla voice assistant, she is in another repository')
            else:
                engine.say("Sorry, couldn't get you :( ")
        
    else :
        # vocalize text output 
        engine.say(text)
    engine.runAndWait()
    return False


# for displaying images, given resolution(type) or name(ctx)
def image(type, ctx=None):
    '''
    This function extracts image to usuable format and displays them. 
    '''
    if (type>5 or type<=0):
        return True 
    elif type == 5:
        ctx.replace("comma", ',')
        txt = '?'+ctx
    else: 
        # type 0-4 have default resolutions to choose from
        list1 = ['1280x720', '1920x1080', '2048x1080', '5096x2160']
        txt = list1[type-1]
    
    # display image
    response = requests.get("https://source.unsplash.com/random/{0}".format(txt))
    file = open('container.jpg','wb')
    file.write(response.content)
    img=Image.open(r"container.jpg")
    img.show()
    file.close
    return False


# plays the song(default browser)
def play(song, genre=None, artist=None, lyrist=None):
    
    '''
    
    This functions plays songs/playlist on user commands.
    
    '''

    if song=="random":
        # code for getting genre/artist/lyrist etc
        # and generating a random playlist.
        # ask if user would like a song or on loop(playlist).
        pass
    # playing via song name
    else:
        talk("playing your requested song "+song+", please wait!")
        print("playing",song)
        pywhatkit.playonyt(song)
    return False


# look up information on wikipedia / gain knowledge
def info(text, search=False, summary=False, line =5, wordCount=20):

    ''' 

    This functions looks information on wikipedia on user commands.

    '''

    if(search):
        information = wikipedia.search(text, wordCount)
    # to look for any information/person/history/reviews etc (summary)
    elif(summary):
        information = wikipedia.summary(text, line)
    print(information)
    talk(information)
    return False



def whatsapp(no="+91 93611 40968"):

    '''

    This function texts whatsapp messages.

    '''
    pywhatkit.sendwhatmsg(no, "hello iam kavi,my boss has told me to text any important info",13, 58)
    print("Successfully Sent!")
    return False


# look for 'place' on google maps
def locate(place):

    '''

    This function looks for places on google maps.

    '''

    talk("user asked to locate "+place)
    webbrowser.open("https://www.google.nl/maps/place/" + place + "")
    return False


# opens files/editors (currently supported : notepad and calculator)
def open(file):

    '''

    This functions opens files/editors.

    '''

    if file == 'calculator':
        subprocess.call("calc.exe")
    else:
        try:
            link = str(file).upper()+".EXE"
            os.startfile(link)
        except:
            talk("could not open the file {file}")
    return False


# get the weather condition (temperature & humidity) of a 'location'
def weather(location):

    '''

    This function shows the weather information.

    '''

    api_key = "51d5d78391e312e72cde67174f38e770"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + location
    result = requests.get(complete_url)
    x = result.json()

    # relaying the output to user
    if x["cod"] != "404":
        weather = x["main"]
        talk("Temperature of " + str(location) + " in kelvin unit is " +
            str(weather['temp']) +
            "\n humidity in percentage is " +
            str(weather['humidity']) +
            "\n description  " +
            str(x['weather'][0]['description']))

        print(str(location) + " Temperature in kelvin unit = " +
            str(weather['temp']) +
            "\n humidity (in percentage) = " +
            str(weather['humidity']) +
            "\n description = " +
            str(x['weather'][0]['description']))
    else: 
        talk("Sorry, there was some error. Please try again later or look for the weather of a different location")
        print("Sorry, there was some error. Please try again later or look for the weather of a different location")
    return False


def health(ctx):

    '''

    This function shows details of memory consumption of voice assistant.

    '''

    pid = os.getpid()
    py = psutil.Process(pid)
    memory_use = py.memory_info()[0] / 2. ** 30
    talk("I use {0:.2f} GB..".format(memory_use))
    return False


def IP(ctx):

    '''

    This function provides IP Address of the user.

    '''

    ip_address=requests.get('https://api64.ipify.org?format=json').json()
    ip=ip_address
    print(f'Your ip address is :- {ip["ip"]}')
    talk(f'Your ip address is :- {ip["ip"]}') 
    return False



def wishMe():

    '''

    wishes the user according to time.

    '''

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
       talk("Good Evening!") 
    return 


# coin flipping game
def flip_a_coin(ctx):

    '''

    This function generates random coin side.

    '''

    mapping = {0:'head', 1:"tail"}
    key = random.randint(0,1)
    talk(f"It's a {mapping[key]} pal!")
    print(f"It's a {mapping[key]} pal!")
    return False



def lucky_no(ctx):

    '''

    Generates any random number between 1 to 10.

    '''
    num = random.randint(1,10)
    print(f"{num} is your lucky number.")
    talk(f"{num} is your lucky number.")
    return False


# volume control
def volume_increaser(ctx):
    '''

    increases volume

    '''
    import pyautogui
    pyautogui.press('volumeup')
    return False

def volume_decreaser(ctx):
    '''

    decreases volume

    '''
    import pyautogui
    pyautogui.press('volumedown')
    return False

def volume_mute(ctx):
    '''

    mutes on command

    '''
    import pyautogui
    pyautogui.press('volumemute')
    return False
    

# battery status
def battery_status(ctx):

    '''

    shows battery status details

    '''

    battery=psutil.sensors_battery()
    percentage=battery.percent
    talk(f"we have {str(percentage)} percent of battery left")
    print(f"we have {percentage} percent of battery left")
    return False
    

# Fetches jokes
def get_joke():

    '''

    This function tells jokes to user.

    '''

    url = 'https://v2.jokeapi.dev/joke/Any'
    response = requests.get(url)
    jokes = response.json()
    joke = 'The funniest thing about APIs is that they never work on time.'
    if jokes['error'] == False:
        if jokes['type'] == 'single':
            joke = jokes['joke'].replace('\"', '')
        else:
            joke = jokes['setup'].replace(
                '\"', '') +'\n'+ jokes['delivery'].replace('\"', '')
    return joke



def intro():

    '''

    This function introduces Kavi to users.

    '''

    print('Hi, this is your voice assistant Kavi')
    talk('Hi, this is your voice assistant Kavi.')
    print('What can i do for you?')
    talk('What can i do for you buddy?')
    talk("")
    return 

def fly_away_bird_game(ctx):
      '''
      This function plays fly away bird game with the user

      '''

      fly_away_bird_dict = {'dog':'pass', 'snake':'pass', 'bee':'fly', 'dragonfly':'fly', 'sparrow':'fly', 'ostrich':'pass', 'lizard':'pass', 'eagle':'fly', 'crow':'fly', 'parrot':'fly', 'tortoise':'pass', 'squirrel':'pass', 'shark':'pass', 'penguin':'pass', 'bat':'fly', 'vulture':'fly', 'earthworm':'pass', 'frog':'pass', 'swan':'fly', 'butterfly':'fly', 'peacock':'fly', 'owl':'fly'}   #assistant uses this to play with user

      #Instructions of the game
      talk('Welcome to the Fly Away Bird Game. Just say fly if flies and pass if not.')
      print('Welcome to the Fly Away Bird Game. Just say fly if flies and pass if not.')
      mixer.music.load('./start.mp3')
      mixer.music.play()
      pygame.time.wait(1)

      #local variables for game to count
      game_round_count = 0
      user_game_score = 0 

      while game_round_count < 15:
            assistant_choice = random.choice(list(fly_away_bird_dict.keys()))
            talk(f"{assistant_choice} fly")
            game_round_count +=1
            user_choice = str(take_command()).lower()
            if user_choice == str(fly_away_bird_dict.get(assistant_choice)):
                  mixer.music.load('./correct.mp3')
                  mixer.music.play()
                  user_game_score +=1
                  pygame.time.wait(2)
            elif user_choice != str(fly_away_bird_dict.get(assistant_choice)) and user_choice == 'pass' or user_choice == 'fly':
                  mixer.music.load('./wrong.mp3')
                  mixer.music.play()
                  pygame.time.wait(2)
                  talk("I don't think so.")
            else:
                  print("Could not recognized")

      #scorecard of game
      if user_game_score >= 12:
            mixer.music.load('./celebration.mp3') # plays celebration song
            talk(f"You are a champ. You got {user_game_score} out of 15 rounds correct.")
            mixer.music.play()
            print(f"Score: {user_game_score}")
      elif user_game_score >= 8:
            talk(f'Well played. You got {user_game_score} out of 15 rounds correct.')
            print(f"Score: {user_game_score}")
      else:
            talk(f'Try harder, you will be best. You got {user_game_score} out of 15 rounds correct.')
            print(f"Score: {user_game_score}")
