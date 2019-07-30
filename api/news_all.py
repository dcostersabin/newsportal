from newsapi import NewsApiClient


def __api_key():
    key = 'e0d3ec8f0c0140f6b99146bf9e4469d7'
    return key


def get_all():
    news_api = NewsApiClient(api_key=__api_key())
    top_headlines = news_api.get_top_headlines(sources='bbc-news,abc-news,abc-news-au,Aftenposten,al-jazeera-english',
                                               language='en')
    return top_headlines


def category(cat, qty):
    news_api = NewsApiClient(api_key=__api_key())
    news_category = news_api.get_top_headlines( category=cat, page_size=qty, language='en')
    return news_category
