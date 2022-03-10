
import speech_recognition as sr
from Features.speak import speak
# from speak import speak
from serpapi import GoogleSearch
# from config import serp_api_id
serp_api_id = "50efe51a6dc4385537bad7b576ae20f16c6e20bb97eafc734be4e0ac63dd4b73"
# serp_api_id =  "92634d753e34b284b752cf279deff86eadc57fb0438b0082937be71dd5c95f17"

#def auto_correct(query):
#    params = {
#    "q": query,
#    "hl": "en",
#    "gl": "us",
#    "api_key": serp_api_id
#    }
#
#    search = GoogleSearch(params)
#    results = search.get_dict()
#    print(results)
#    search_information = results['search_information']
#    print(search_information)
#    try:
#      return search_information['spelling_fix']
#    except:
#        return query

def auto_correct(query):  #serpapi
    params = {
    "q": query,
    "hl": "en",
    "gl": "us",
    "api_key": serp_api_id
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    search_information = results['search_information']
    try:
      return search_information['spelling_fix']
    except:
        return query
class countcalls(object):
   "Decorator that keeps track of the number of times a function is called."

   __instances = {}

   def __init__(self, f):
      self.__f = f
      self.__numcalls = 0
      countcalls.__instances[f] = self

   def __call__(self, *args, **kwargs):
      self.__numcalls += 1
      return self.__f(*args, **kwargs)

   def count(self):
      "Return the number of times the function f was called."
      return countcalls.__instances[self.__f].__numcalls

   @staticmethod
   def counts():
      "Return a dict of {function: # of calls} for all registered functions."
      return dict([(f.__name__, countcalls.__instances[f].__numcalls) for f in countcalls.__instances])
  

@countcalls
def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1.2
            r.non_speaking_duration =0.3
            r.energy_threshold = 340
            audio = r.listen(source, phrase_time_limit= 6)
        
            
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language= "en-in")
            print(f"U said: {query}")
        except:
            if listen.count() >=3:
                query = " "
                return query
            speak("Couldn't understand, say that again please!")
            query = listen()
            
        try:
            return (auto_correct(query)).lower()
        except Exception as e:
            print("Exception: ", e)
            return query.lower()
        


# def listen():
#     for _ in range(3):
#         query = listen_recur()
#         try:
#             return (auto_correct(query)).lower()
#         except Exception as e:
#             print("Exception: ", e)
#             return query.lower()
        
        
        
def listen_std():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        r.non_speaking_duration =0.3
        r.energy_threshold = 340
        audio = r.listen(source, phrase_time_limit= 6) 
        
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= "en-in")
        print(f"U said: {query}")
    except:
        query = ""
    return query.lower()
    # return (auto_correct(query)).lower()

#auto_correct("he es a gret persn")