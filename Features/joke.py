from pyjokes import get_joke
from random import randint
from Features.speak import speak
'''
returns  a joke in string format
you can also add custom jokes in the list
'''
joke_list=[]

def startJoke():
    joke=get_joke()
    joke_list.append(joke)
    speak(joke_list[randint(0,len(joke_list)-1)])

