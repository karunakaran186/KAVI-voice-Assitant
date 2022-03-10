
import pyttsx3
def speak(audio):
    engine = pyttsx3.init('sapi5') #google API
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200 )  # rate by default is 200
    print(f"A.I : {audio}")
    engine.say(text = audio)
    engine.runAndWait()
    print(" ")
# from gtts import gTTS
# from playsound import playsound
# def speak(audio):
#     """
#     This function adds google assistant voice to our function incase of any hindi input it can also give hindi output un-comment the given line to listen hindi speech
#     """
#     engine = gTTS(audio)
#     engine.save('Assis.mp3')
#     playsound('Assis.mp3')
