from Features.speak import speak
from Features.listen import listen
import datetime
from word2number import w2n
def set_alarm():
    speak("ok,what hour you want to set the alarm..?")
    try:
        alarmH=w2n.word_to_num(listen())
    except Exception as e:
        print(e)
        speak("please, say that again")
        alarmH=w2n.word_to_num(listen())
    finally:
            speak("Unable to understand, kindly retry")
    
    
                 
    speak("ok,what minute you want to set the alarm..?")
    alarmM = w2n.word_to_num(listen())        
    speak("Should I set it for eh em or Pm ?")
    ampm = str(listen())      
    speak(f"Ok sir,Setting your alarm for, {alarmH}:{alarmM}:{ampm}")
    speak("Alarm set...")

    if(ampm=='pm'):
        alarmH=alarmH+12
        f =1;
        while f:
            if (alarmH== datetime.datetime.now().hour and alarmM==datetime.datetime.now().minute):
                speak("Alarm Time sir, Please Wake up....I repeat, Alarm Time sir, Please Wake up ")
                said =  listen()
                if said == "stop" or "pause" or "quite": 
                    f =0;
                    
                # speak("Please Wake up sir")
                            # print("Time to wake up sir...")
                            # subprocess.call(["afplay", "beep_sound.mp3"])
