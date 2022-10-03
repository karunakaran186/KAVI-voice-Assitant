# importing functions and libraries
from modules import *
import speech_recognition as sr
import pyttsx3
import sys

#from email.mime import audio
#from numpy import place
#from setuptools import Command


# mapping of -- to functions
mapping = {'play': play, 'listen': play, 'images': image, 'where is': locate,
           'locate': locate, 'whatsapp': whatsapp, 'open': open, 'weather': weather,
           'who is': info, 'search': info, 'movie review': info, 'history': info, 'get my ip': IP,
           'flip a coin': flip_a_coin, 'pick': lucky_no, 'choose': lucky_no, 'health of kavi': health,
           'volume up': volume_increaser, 'increase the volume': volume_increaser, 'volume down': volume_decreaser,
           'decrease the volume': volume_decreaser, 'mute': volume_mute, 'how much power left': battery_status, 'battery': battery_status, 'show notes': show_notes, 'take notes': take_notes, 'read pdf': read_pdf_file
           }


# setting up the listener and speaker
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 6.0)


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


def choose(command):
    '''
    This function choose the command according to mapping.
    '''

    for key in mapping.keys():
        if key in command:
            return key, mapping[key]
    else:
        return '', talk


def capital(state):
    if state == 'Andra Pradesh':
        talk('Amaravati')
    elif state == 'Arunachal Pradesh':
        talk('Itanagar')
    elif state == 'Assam':
        talk('Dispur')
    elif state == 'Bihar':
        talk('Patna')
    elif state == 'Chhattisgarh':
        talk('Raipur')
    elif state == 'Goa':
        talk('Panaji')
    elif state == 'Gujarat':
        talk('Gandhinagar')
    elif state == 'Haryana':
        talk('Chandigarh')
    elif state == 'Himachal Pradesh':
        talk('Shimla')
    elif state == 'Jharkhand':
        talk('Ranchi')
    elif state == 'Karnataka':
        talk('Bengaluru')
    elif state == 'Kerala':
        talk('Thiruvananthapuram')
    elif state == 'Madhya Pradesh':
        talk('Bhopal')
    elif state == 'Maharashtra':
        talk('Mumbai')
    elif state == 'Manipur':
        talk('Imphal')
    elif state == 'Meghalaya':
        talk('Shillong')
    elif state == 'Mizoram':
        talk('Aizawl')
    elif state == 'Nagaland':
        talk('Kohima')
    elif state == 'Odisha':
        talk('Bhubaneswar')
    elif state == 'Punjab':
        talk('Chandigarh')
    elif state == 'Rajasthan':
        talk('Jaipur')
    elif state == 'Sikkim':
        talk('Gangtok')
    elif state == 'Tamil Nadu':
        talk('Chennai')
    elif state == 'Telangana':
        talk('Hyderabad')
    elif state == 'Tripura':
        talk('Agartala')
    elif state == 'Uttar Pradesh':
        talk('Lucknow')
    elif state == 'Uttarakhand':
        talk('Dehradun in Winter and Gairsain in Summer')
    elif state == 'West Bengal':
        talk('West Bengal')
    elif state == 'Andaman and Nicobar Islands':
        talk('Andaman and Nicobar Islands')
    elif state == 'Dadra & Nagar Haveli and Daman & Diu':
        talk('Daman')
    elif state == 'Delhi':
        talk('Delhi')
    elif state == 'Jammu and Kashmir':
        talk('Srinagar in Summer and Jammu in Winter')
    elif state == 'Lakshadweep':
        talk('Kavaratti')
    elif state == 'Puducherry':
        talk('Pondicherry')
    elif state == 'Ladakh':
        talk('Leh')
    elif state == 'India':
        talk('New Delhi')
    else:
        talk('Please say that again...')


def tell_month():
    dt = datetime.datetime.today()
    m_onth = dt.month
    if m_onth == 1:
        talk("it's january")
    if m_onth == 2:
        talk("it's february")
    if m_onth == 3:
        talk("it's march")
    if m_onth == 4:
        talk("it's april")
    if m_onth == 5:
        talk("it's may")
    if m_onth == 6:
        talk("it's june")
    if m_onth == 7:
        talk("it's july")
    if m_onth == 8:
        talk("it's august")
    if m_onth == 9:
        talk("it's september")
    if m_onth == 10:
        talk("it's october")
    if m_onth == 11:
        talk("it's november")
    if m_onth == 12:
        talk("it's december")


def tell_day():
    now = datetime.datetime.now()
    ans = (now.strftime("%A"))
    talk(ans)


def func():
    '''
    This function takes the user's command continuously till the user want to quit.
    '''

    talk("Tell me! How can I help you?")
    print("Tell me! How can I help you?")
    command = take_command().lower()
    if 'exit' in command or 'stop' in command or 'shutdown' in command or 'quit' in command:
        return False
    else:
        key, task = choose(command)
        notdone = True
        # see if the task is done or not.
        while(notdone):
            # in done, take in the next command
            # if not done, try doing it again or provide the error

            if key == '':
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
                    if type == 5:
                        talk("speak keywords seperated by commas ")
                        ctx = take_command()
                except:
                    print(
                        "Sorry, couldn't register your choise. Please type it instead")
                    talk("Sorry, couldn't register your choise. Please type it instead")
                    try:
                        type = int(input())
                        if type == 5:
                            talk("speak keywords seperated by commas ")
                            ctx = take_command()
                    except:
                        type = -1
                        print("not a valid choise")
                notdone = task(type, ctx)
            elif task == info:
                try:
                    if key == 'search':
                        notdone = task(command.replace(key, ''), search=True)
                    else:
                        notdone = task(command.replace(key, ''), summary=True)
                except wikipedia.exceptions.WikipediaException:
                    talk("Pardon me, but search for what ?")
                    print("Pardon me, but search for what ?")
                    return True
            # no for whattsapp?
            elif key == 'whatsapp':
                notdone = task()
            elif key == 'weather':
                place = take_command()
                notdone = task(place)
              # take notes
            elif key == 'take notes':
                print('..')
                take_notes()
                print('Noted!!')
              # show notes
            elif key == 'show notes':
                print('..')
                show_notes()
                print('Done')
            elif key == 'capital':
                fun_talk('Which state capital you want to know')
                query = get_command()
                notdone = capital(query)

            elif key == 'month':
                tell_month()

            elif key == 'day' or key == 'today':
                tell_day()

            elif key == 'read pdf':
                read_pdf_file()

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
