import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from django.shortcuts import render
from . import models

# Create your views here.

BASE_URL = 'https://kolkata.craigslist.org/search/jjj?query={}'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    # python dictionary get function
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    # print(quote_plus(search))
    # dynamically created base url and the searches are just added to it
    final_url = BASE_URL.format(quote_plus(search))
    # print(final_url)
    response = requests.get(final_url)
    data = response.text
    # print(data)
    # parsing html data into the soup object by Beautiful Soup
    soup = BeautifulSoup(data, features='html.parser')
    # post_titles = soup.find_all('a', {'class': 'result-title'})
    # print(post_titles[0].get('href'))
    post_listings = soup.find_all('li', {'class': 'result-row'})
    # title texts only
    # post_titles = post_listings[0].find(class_='result-title').text
    # link only
    # post_url = post_listings[0].find('a').get('href')
    # price only
    # post_price = post_listings[0].find(class_='result-price').text
    # print(post_titles)
    # print(post_url)
    # print(post_price)
    final_postings = []
    for post in post_listings:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        final_postings.append((post_titles, post_url))
    front_end_stuff = {
        'search': search,
        'final_postings': final_postings,
    }
    return render(request, 'my_app/new_search.html', front_end_stuff)
