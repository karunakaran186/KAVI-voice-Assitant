# importing the libraries 
import os
import subprocess
from PIL import Image
import wikipedia
import pywhatkit
import pyttsx3
import webbrowser
import requests
import psutil
import pyjokes
import datetime
import random
import cv2
import numpy as np
import pyautogui


# setting the engine properties like voice and volumne
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# main talk function, that will be used to provide voice output to the user
def talk(text=None, ques=None):
    if text==None:
        # simple talk responses (input => ques)
        if(ques!=None):  
            # talk to kavi like a buddy :)
            if 'are you single' in ques :
                engine.say('no......um.i am in relationship with wireless devices')
            elif 'do you like me' in ques:
                engine.say('yes boss definitely')
            elif 'what is your name' in ques:
                engine.say('My devloper karunakran has named me kkavi')
            elif 'cringe' in ques:
                engine.say('alright........he/she was funniest perosn')
            elif 'joke' in ques:
                joke = pyjokes.get_joke()
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
                engine.say('her name is nilla voice assistant, she was in another repository')
            else:
                engine.say("Sorry, couldn't get you :( ")
        
    else :
        # vocalize text output 
        engine.say(text)
    engine.runAndWait()
    return False


# for displaying images, given resolution(type) or name(ctx)
def image(type, ctx=None):
    # extract image requirements to usable format
    if (type>5 or type<=0):
        return True 
    elif type ==5:
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


# playing the song on default browser
def play(song, genre=None, artist=None, lyrist=None):
    # to play random playlist, based on (genre/artist/lyrist)
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
    # to look for varieties/search results(search)
    if(search):
        information = wikipedia.search(text, wordCount)
    # to look for any information/person/history/reviews etc (summary)
    elif(summary):
        information = wikipedia.summary(text, line)
    print(information)
    talk(information)
    return False


# sent msgs on wattsapp, after providing the number(no) and text(default as of now)
def whattsapp(no="+91 93611 40968"):
    # default test 'hello iam kavi,my boss has told me to text any important info'
    pywhatkit.sendwhatmsg(no, "hello iam kavi,my boss has told me to text any important info",13, 58)
    print("Successfully Sent!")
    return False


# look for 'place' on google maps
def locate(place):
    talk("user asked to locate "+place)
    webbrowser.open("https://www.google.nl/maps/place/" + place + "")
    return False


# opening some file/editor on the users computer. (currently supported : notepad and calculator)
def open(file):
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
    # extracting weather 
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


# provide the memory consumption of the voice assistant
def health(ctx):
    pid = os.getpid()
    py = psutil.Process(pid)
    memory_use = py.memory_info()[0] / 2. ** 30
    talk("I use {0:.2f} GB..".format(memory_use))
    return False


# provide the ip address of the user
def IP(ctx):
    ip_address=requests.get('https://api64.ipify.org?format=json').json()
    ip=ip_address
    print(f'Your ip address is :- {ip["ip"]}')
    talk(f'Your ip address is :- {ip["ip"]}') 
    return False


# for greetings
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
       talk("Good Evening!") 
    return 


# coin flipping 
def flip_a_coin(ctx):
    mapping = {0:'head', 1:"tail"}
    key = random.randint(0,1)
    talk(f"It's a {mapping[key]} pal!")
    print(f"It's a {mapping[key]} pal!")
    return False


# choosing a random no for the user
def lucky_no(ctx):
    num = random.randint(1,10)
    print(f"{num} is your lucky number.")
    talk(f"{num} is your lucky number.")
    return False


# introduction for the beginning of the application
def intro():
    print('hello iam kavi Voice assistant')
    talk('hello iam kavi')
    print('How are you buddy!!!')
    talk('How are you buddy!!!')
    print('doing good right?????')
    talk('doing good right?????')
    print('think so good')
    talk('think so good')
    print('what can i do for you buddy')
    talk('what can i do for you buddy')
    talk("")
    return 

def screen_record(key):                                                                    #Screen Recording function              

    print("Started Screen recording")                                                                        
    talk("started screen recording press q to stop and continue")
    user = psutil.users()[0].name                                                       #gets the user name 
    f_path = "C:\\Users\\" + user + "\\Desktop"       
    # f_path = input("Enter where u want to save the file")                             #can also have an option as to where the user wants to save the file
    if os.path.exists(f_path):
        save_file = os.path.join(f_path,"output.mp4")                                   #saves the file in the corresponding directory
    else:
        save_file ="output.mp4"                                                         # if path not found saves path in the current directory

    s_size = (1920,1080)
    fps = 10.0                                                                          #determines how fast the slow the playback speed will be

    fcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(save_file,fcc,fps,(s_size))

    while 1:

        img = pyautogui.screenshot()
        frm = np.array(img)
        frm = cv2.cvtColor(frm,cv2.COLOR_BGR2RGB)
        cv2.imshow("recorder",frm)
        cv2.namedWindow("recorder",cv2.WINDOW_NORMAL)
        cv2.resizeWindow("recorder", 800,800)
        out.write(frm)
        
        key = cv2.waitKey(1)                                                             # q to close the window and stop recording
        if key == 113:
            break

    cv2.destroyAllWindows()
    out.release()
