# importing functions and libraries
from modules import *
import pyttsx3
import sys

#from email.mime import audio
#from numpy import place
#from setuptools import Command


# mapping of -- to functions
mapping = {'play':play, 'listen':play, 'images':image, 'where is':locate,
    'locate':locate, 'whatsapp':whatsapp, 'open':open, 'weather':weather,
    'who is':info, 'search':info, 'movie review':info, 'history':info, 'get my ip':IP,
    'flip a coin':flip_a_coin, 'pick':lucky_no, 'choose':lucky_no, 'health of kavi':health,
     'volume up':volume_increaser,'increase the volume':volume_increaser,'volume down':volume_decreaser,
     'decrease the volume':volume_decreaser,'mute':volume_mute,'how much power left':battery_status,'battery':battery_status, 'fly away bird': fly_away_bird_game,
}
 

# setting up the listener and speaker
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume',6.0) 


def choose(command):
    '''
    This function choose the command according to mapping.
    '''

    for key in mapping.keys():
        if key in command:
            return key, mapping[key]
    else:
        return '', talk



def func():
    '''
    This function takes the user's command continuously till the user want to quit.
    '''
    
    talk("Tell me! How can I help you?")
    print("Tell me! How can I help you?")
    command = take_command().lower()
    if 'exit' in command or 'stop' in command or 'shutdown' in command or 'quit' in command:
        return False 
    else :
        key, task = choose(command)
        notdone =True
        # see if the task is done or not. 
        while(notdone):
            # in done, take in the next command
            # if not done, try doing it again or provide the error 

            if key=='':
                notdone = task(ques=command)
            elif key == 'images':
                # provide option in frontend instead 
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
                try:
                    ctx = None
                    type = int(take_command())
                    if type==5:
                        talk("speak keywords seperated by commas ")
                        ctx=take_command()
                except:
                    print("Sorry, couldn't register your choise. Please type it instead")
                    talk("Sorry, couldn't register your choise. Please type it instead")
                    try:
                        type = int(input())
                        if type==5:
                            talk("speak keywords seperated by commas ")
                            ctx=take_command()
                    except:
                        type = -1
                        print("not a valid choise")
                notdone = task(type, ctx)
            elif task == info:
                if key == 'search':
                    notdone = task(command.replace(key, ''), search=True)
                else :
                    notdone = task(command.replace(key, ''), summary=True)
            # no for whattsapp?
            elif key == 'whatsapp':
                notdone = task()
            elif key == 'weather':
                place = take_command()
                notdone = task(place)
            else:
                notdone = task(command.replace(key, '').lstrip())
        
        return True


# running loop of the main function 
if __name__ == '__main__':
    intro()
    x = True
    while x:  
        wishMe()
        x = func() 
    print("byee!!")
