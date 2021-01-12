from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'HOME'
    }

    return render(request,'index.html',context)