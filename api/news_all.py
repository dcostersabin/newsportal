from newsapi import NewsApiClient


def __api_key():
    # key = 'e0d3ec8f0c0140f6b99146bf9e4469d7'
    key = '657a010b291d44b29c0bea510c097299'
    return key


def get_all():
    news_api = NewsApiClient(api_key=__api_key())
    top_headlines = news_api.get_top_headlines(sources='bbc-news,abc-news,the-verge,Aftenposten,al-jazeera-english',
                                               language='en')
    return top_headlines


def category(cat, qty):
    news_api = NewsApiClient(api_key=__api_key())
    news_category = news_api.get_top_headlines(category=cat, page_size=qty, language='en')
    return news_category


def sources(sou, qty):
    news_api = NewsApiClient(api_key=__api_key())
    news_sources = news_api.get_top_headlines(sources=sou, page_size=qty, language='en')
    return news_sources


def get_source():
    news_api = NewsApiClient(api_key=__api_key())
    news_sources = news_api.get_sources()
    return news_sources['sources']

def query(keyword):
    news_api = NewsApiClient(api_key=__api_key())
    data = news_api.get_everything(q=keyword)
    return data
