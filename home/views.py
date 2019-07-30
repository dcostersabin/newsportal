from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from api import news_all as news
import json


# Create your views here.
def index(request):
    top_news = news.get_all()
    index_page = loader.get_template("index.html")
    top_six = {
        'first' : top_news['articles'][0],
        'second': top_news['articles'][1],
        'third': top_news['articles'][2],
        'fourth': top_news['articles'][3],
        'fifth': top_news['articles'][4],
        'sixth': top_news['articles'][5],
    }

    business = news.category('business', 8)
    general = news.category('general', 8)
    health = news.category('health', 8)
    science = news.category('science', 8)

    context = {'news': top_news['articles'],
               'top_six': top_six,
               'business': business['articles'],
               'general': general['articles'],
               'health':health['articles'],
               'science':science['articles']
               }

    return HttpResponse(index_page.render(context, request))

