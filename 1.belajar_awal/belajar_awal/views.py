from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'nav': [
            ['/', 'home'],
            ['/blog', 'blog'],
            ['/about', 'about'],
        ],
    }
    return render(request, 'index.html', context)
