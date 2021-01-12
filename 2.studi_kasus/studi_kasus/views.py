from django.shortcuts import render


def index(request):
    context = {
        'Judul':'Home Page',
        'Content':'ini adalah halaman home '
    }

    return render(request,'index.html',context)