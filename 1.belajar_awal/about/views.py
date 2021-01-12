from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'nav': [
            ['/', 'home'],
            ['/blog/cerita', 'cerita'],
            ['/blog/news', 'news'],
        ],
    }
    return render(request, "about/index.html", context)
