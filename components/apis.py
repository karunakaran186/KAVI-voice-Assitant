import requests

def getJoke():
    url = 'https://v2.jokeapi.dev/joke/Any'
    response = requests.get(url)
    jokes = response.json()
    joke = 'The funniest thing about APIs is that they never work on time.'
    if jokes['error'] == False:
        if jokes['type'] == 'single':
            joke = jokes['joke'].replace('\"', '')
        else:
            joke = jokes['setup'].replace(
                '\"', '') + jokes['delivery'].replace('\"', '')
    return joke


def getWikipedia(TOPIC):
    S = requests.Session()
    URL = 'https://en.wikipedia.org/api/rest_v1/page/summary/'+ TOPIC
    R = S.get(url=URL)
    DATA = 'The wikimedia server is likely to be down.'
    if R.status_code == 200:
        DATA = R.json()['extract']
    print(DATA)
