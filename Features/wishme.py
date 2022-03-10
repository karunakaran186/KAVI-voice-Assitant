from Features.speak import speak
import datetime

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning sir, I'm ready. You can call me anytime")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, I'm ready. You can call me anytime")
    else:
        speak("Good Evening sir, I'm ready. You can call me anytime")
    

