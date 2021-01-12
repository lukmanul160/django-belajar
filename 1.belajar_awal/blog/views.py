from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'judul': 'blog',
        'kontributor': 'lukman',
        'nav': [
            ['/', 'home'],
            ['/blog/cerita', 'cerita'],
            ['/blog/news', 'news'],
        ],
    }
    return render(request, 'blog/index.html', context)


def news(request):
    context = {
        'judul': 'news',
        'kontributor': 'sukirman',
    }
    return render(request, 'blog/index.html', context)


def cerita(request):
    context = {
        'judul': 'cerita',
        'kontributor': 'sukijan',
    }
    return render(request, 'blog/index.html', context)
