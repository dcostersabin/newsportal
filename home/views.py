from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from api import news_all as news
from django.contrib.auth.decorators import login_required
from .models import Interest
from api import user_specific
from django.contrib import messages


# Create your views here.
def index(request):
    top_news = news.get_all()
    index_page = loader.get_template("index.html")
    top_six = {
        'first': top_news['articles'][0],
        'second': top_news['articles'][1],
        'third': top_news['articles'][2],
        'fourth': top_news['articles'][3],
        'fifth': top_news['articles'][4],
        'sixth': top_news['articles'][5],
    }

    business = news.category('business', 20)
    general = news.category('general', 20)
    health = news.category('health', 20)
    science = news.category('science', 20)
    sports = news.category('sports', 20)
    entertainment = news.category('entertainment', 20)
    technology = news.category('technology', 20)
    context = {'news': top_news['articles'],
               'top_six': top_six,
               'business': business['articles'],
               'general': general['articles'],
               'health': health['articles'],
               'science': science['articles'],
               'sports': sports['articles'],
               'entertainment': entertainment['articles'],
               'technology': technology['articles'],

               }

    return HttpResponse(index_page.render(context, request))


@login_required
def personal(request):
    users = request.user
    check = Interest.objects.filter(user=users).exists()
    top_news = news.get_all()
    if check:
        interest = Interest.objects.get(user=users)
        category = interest.category
        sources = interest.sources
        results = user_specific.personal(sources)
        user_cat_news = {}
        for cats in category.split(','):
            temp = (news.category(cats, 20))
            user_cat_news[cats] = temp['articles']
        if results:
            return render(request, 'personal.html',
                          {'context': results, 'cat': category.split(','), 'sou': sources, 'news': top_news['articles'],
                           'cat_news': user_cat_news})
        else:
            return render(request, 'personal.html', {'context': 'error'})
    else:
        return render(request, 'personal.html', {'context': 'error'})


@login_required
def edit(request):
    users = request.user
    check = Interest.objects.filter(user=users).exists()
    if check:
        interest = Interest.objects.get(user=users)
        user_category = interest.category
        user_sources = interest.sources
    else:
        user_sources = ''
        user_category = ''

    top_news = news.get_all()
    sources = news.get_source()
    all_category = ['business', 'health', 'general', 'science', 'sports', 'technology', 'entertainment']
    return render(request, 'customize.html',
                  {'news': top_news['articles'], 'sources': sources, 'user_source': user_sources,
                   'user_category': user_category, 'all_category': all_category})


@login_required
def submit_source(request):
    users = request.user
    check = Interest.objects.filter(user=users).exists()
    if check:
        interest = Interest.objects.get(user=users)
        user_source = interest.sources
        if request.POST['source_id'] in user_source:
            messages.info(request, 'Source Already Selected')
            return redirect('edit')
        else:
            user_source = user_source + ',' + request.POST['source_id']
            update = Interest.objects.get(user=users)
            update.sources = user_source
            update.save()
            messages.success(request, 'Source Updated SuccessFully')
            return redirect('edit')
    else:
        insert = Interest(sources=request.POST['source_id'], user=users)
        insert.save()
        messages.success(request, 'Source Successfully Updated')
        return redirect('edit')


@login_required
def submit_category(request):
    users = request.user
    check = Interest.objects.filter(user=users).exists()
    if check:
        interest = Interest.objects.get(user=users)
        user_category = interest.category
        if request.POST['category_id'] in user_category:
            messages.info(request, 'Category Already Selected')
            return redirect('edit')
        else:
            user_category = user_category + ',' + request.POST['category_id']
            update = Interest.objects.get(user=users)
            update.category = user_category
            update.save()
            messages.success(request, 'Category Updated SuccessFully')
            return redirect('edit')
    else:
        insert = Interest(sources=request.POST['category_id'], user=users)
        insert.save()
        messages.success(request, 'Category Successfully Updated')
        return redirect('edit')


@login_required
def search(request):
    top_news = news.get_all()
    data = news.query(request.POST['query'])
    return render(request, 'search.html', {'news': top_news['articles'], 'query':data['articles'],'key':request.POST['query']})
