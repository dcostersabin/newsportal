from newsapi import NewsApiClient


def __api_key():
    key = 'e0d3ec8f0c0140f6b99146bf9e4469d7'
    return key


def personal(cat, sour):
    news_api = NewsApiClient(api_key=__api_key())
    sources_news = news_api.get_top_headlines(sources=sour)
    category_news = news_api.get_top_headlines(category=cat)
    result = {
        'sources': sources_news['articles'],
        'category': category_news['articles']
    }
    return result
