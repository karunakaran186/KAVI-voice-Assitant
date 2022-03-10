import requests
import json
NEWS_API_KEY="8f6bbf4ba75a402fbfbe8e12704272e2"


def more_news():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=8f6bbf4ba75a402fbfbe8e12704272e2'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?country=in&apiKey=8f6bbf4ba75a402fbfbe8e12704272e2'


def get_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

