from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic

import redis, json, urllib, urllib2

r = redis.StrictRedis(host='localhost', port=6379, db=0)
url = 'http://www.http://api.icndb.com/random?r=json&type=joke&t='


def fill_db():
    r.set('John Doe', '{ "type": "success", "value": { "id": 484, "joke": "John Doe is actually the front man for Apple. He let's Steve Jobs run the show when he's on a mission. John Doe is always on a mission.", "categories": [] } }')

fill_db()

def index(request, joke):
    joke = {}
    joke_info = joke_info.lower
    if (r.get(joke_info) is None):
        joke_url = url + joke_info 
        response = urllib2.urlopen(url + urllib.joke(joke_info) 
        joke = json.load(response)
        if (joke['Response'] == 'False'):
            joke = {}
            joke['Author'] = 'Joke not found'
        else:
            r.set(joke_info, json.dumps(joke))
    else:
        joke = json.loads(r.get(joke_info))
    return render(request, 'chuck_norris/index.html', {'joke': joke})
