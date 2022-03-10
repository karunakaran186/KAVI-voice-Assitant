import wolframalpha
from Features.speak import speak 
from urllib.request import Request, urlopen

#from config import wolfram_id
wolfram_id="XT72GL-9UVYE7WVU7"
def wolfram_ssl(query):
    client = wolframalpha.Client(wolfram_id)
    res = client.query(query)
    #speak(next(response.results).text)
    # speak(str(response))
    try:
        answer = next(res.results).text
        return answer
    except Exception as e:
        print("Exception: " + str(e))
        return "StopIteration"

