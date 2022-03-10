
# elif 'amazon.com' in said:
#             speak("ok,opening Amazon Website")
#             # print("Opening Amazon...")
#             webbrowser.open('https://www.amazon.in/')
import webbrowser
#from Alexa_Assistant_Original.fakess import speak
import speak
def open_website(query, website):
    website = query.replace("open", "").replace("search", "")
    speak(f"Opening {website}")
    webbrowser.open(website)

def website_open(query):
    """
    Please put the respective link the the open_website function
    """
    if "youtube" or "youtube.com"  in query :
        open_website("https://www.youtube.com/") #Place your website here
    elif "amazon" or "amazon.com" in query:
        open_website('https://www.amazon.in/')
    elif "flipkart" or "flipkart.com" in query:
        open_website("https://www.flipkart.com/")
    elif "gmail" or "gmail.com" or "mail" or "inbox" in query:
        open_website("https://mail.google.com/mail/u/0/")
    
    
    
    