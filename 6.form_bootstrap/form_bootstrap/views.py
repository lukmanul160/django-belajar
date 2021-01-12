from django.shortcuts import render

def index(request):
    context = {
        'heading':'HOME',
        'content':'ini content HOME',
    }

    return render(request,'index.html',context)