import os
import subprocess
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import wikipedia
import webbrowser
import requests
import psutil
import datetime
from email.mime import audio
from numpy import place
from PIL import Image
from setuptools import Command
import cv2
import pyautogui
import numpy as np
import random


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def img_requests(txt):
    response=requests.get("https://source.unsplash.com/random{0}".format(txt))
    file=open('container.jpg','wb')
    file.write(response.content)
    img=Image.open(r"container.jpg")
    img.show()
    file.close


def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
       talk("Good Evening!")      
    


hi = 0

if hi == 0:
    talk('hello iam kavi')
    print('hello iam kavi Voice assistant')
    talk('How are you buddy!!!')
    print('How are you buddy!!!')
    talk('doing good right?????')
    print('doing good right?????')
    talk('think so good')
    print('think so good')
    talk('what can i do for you buddy')
    print('what can i do for you buddy')
    wishMe()
else:
    print('listening')


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        talk("listening.....")
        audio = r.record(source, duration=3)

        try:
            command = r.recognize_google(audio, language='en-in')
            print(f"user said:{command}\n")

        except Exception as e:
            talk("Pardon me,Please say that again")
            print("Pardon me,Please say that again")
            return "Not Found"
            print("command")
        return command


print("Loading your AI personal Assistant kavi")
talk("Loading your AI personal Assistant kavi")


def get_memory_consumption():
    pid = os.getpid()
    py = psutil.Process(pid)
    memory_use = py.memory_info()[0] / 2. ** 30
    return memory_use


def screen_record():                                                                   #Screen Recording function              
                                                                                       
    user = psutil.users()[0].name                                                     #gets the user name 
    f_path = "C:\\Users\\" + user + "\\Desktop"       
    # f_path = input("Enter where u want to save the file")                            #can also have an option as to where the user wants to save the file
    save_file = os.path.join(f_path,"output.mp4")                                      #saves the file in the corresponding directory

    s_size = (1920,1080)
    fps = 30.0                                                                        #determines how fast the slow the playback speed will be

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


if __name__ == '__main__':

    while True:
        talk("Tell me! How can I help you?")
        print("Tell me! How can I help you?")
        command = take_command().lower()

        if "exit" in command or "stop" in command or "shutdown" in command:
            talk("Your AI assistant kavi is shutting down,Good bye and have a good day (:")
            print("Your AI assistant kavi is shutting down,Good bye and have a good day (:")
            break

        elif 'images' in command:
           
            print("""Please provide an option for Image
        # 1, HD Random Picture
        # 2, FHD Random Picture
        # 3, 2K Random Picture
        # 4, 4k Random Picture
        # 5, Picture with User Provided Keywords """)
            talk("""Please provide an option for Image
        # 1, HD Random Picture
        # 2, FHD Random Picture
        # 3, 2K Random Picture
        # 4, 4k Random Picture
        # 5, Picture with User Provided Keywords """)
            ans=take_command()           
            talk("Please wait while we fetch the images from our database.")
            if 'one' in ans or '1' in ans or 'won' in ans:
                img_requests('/1280x720')
            elif 'two' in ans or '2' in ans or 'tu' in ans:            
                img_requests('/1920x1080')
            elif 'three' in ans or '3' in ans or 'tree' in ans or 'free' in ans:
                img_requests('/2048x1080')
            elif 'four' in ans or '4' in ans or 'for' in ans:
                img_requests('/4096x2160')
            elif 'five' in ans or '5' in ans  or 'fibe' in ans:
                talk("speak keywords seperated by commas ")
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
            pywhatkit.sendwhatmsg("+91 93611 40968", "hello iam kavi,my boss has told me to text any important info",
                                  13, 58)
            print("Successfully Sent!")
            continue

        elif 'who is' in command:
            person = command.replace('who is', '')
            source = wikipedia.summary(person, 100)
            print(source)
            talk(source)


        elif 'search' in command:
            info = command.replace('search', '')
            general = wikipedia.search(info, 100)
            print(general)
            talk(general)

        elif 'history' in command:
            gen = command.replace('history, battle, movie review', '')
            small = wikipedia.summary(gen, 100)
            print(small)
            talk(small)

        elif 'movie review' in command:
            movie = command.replace('movie review', '')
            small = wikipedia.summary(movie, 10)
            print(small)
            talk(small)

        elif 'are you single' in command:
            talk('no......um.i am in relationship with wireless devices')
        elif 'do you like me' in command:
            talk('yes boss definitely')
        elif 'what is your name' in command:
            talk('My devloper karunakran has named me kkavi')
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
            try:
                p=subprocess.call('calc.exe')
            except TypeError as e:
                pass
            except FileNotFoundError as e:
                print("File not found in the system!")
                talk("File not found in the system!")

        elif 'open word document' in command:
            talk('Opening Word document')
            try:
                p=os.startfile(r'WordPad.EXE')
                raise p
            except FileNotFoundError as e:
                try:
                    q=os.startfile(r'WINWORD.EXE')
                    raise q
                except TypeError as e:
                    pass
                except FileNotFoundError as e:
                    print("File not found in the system!")
                    talk("File not found in the system!")
            except TypeError as e:
                pass

        elif 'open notepad' in command:
            talk('Open Notepad')
            try:
                p=os.startfile(r'NOTEPAD.EXE')
            except TypeError as e:
                pass
            except FileNotFoundError as e:
                print("File not found in the system!")
                talk("File not found in the system!")

        elif 'get my ip' in command:
            ip_address=requests.get('https://api64.ipify.org?format=json').json()
            ip=ip_address
            print(f'Your ip address is :- {ip["ip"]}')
            talk(f'Your ip address is :- {ip["ip"]}')    

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
        


        elif "screen recording" in command:
            talk('press q to stop and save recording')
            print('press q to stop and save recording')
            screen_record()
            
        elif "flip a coin" in command:
            head = random.randint(0,1)
            if(head):
                talk("It's a head pal!")
                print("It's a head pal!")
            else:
                talk("It's a tail.")
                print("It's a tail")
        elif ("pick" in command and "number"in command) or ("choose" in command and "number" in command):
            num = random.randint(1,10)
            talk(f"{num} is your lucky number.")
            print(f"{num} is your lucky number.")

