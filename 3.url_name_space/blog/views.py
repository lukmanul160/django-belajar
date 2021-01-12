from django.shortcuts import render

# Create your views here.
def khususPost(request,input):
    context = {
        'judul':input,
    }

    return render(request,'blog/index.html',context)

def categoryPost(request):
    context = {
        'judul':'category post',
    }

    return render(request,'blog/index.html',context)

def singelPost(request):
    context = {
        'judul':'single post',
    }

    return render(request,'blog/index.html',context)

def index(request):
    context = {
        'judul':'HOME BLOG',
    }

    return render(request,'blog/index.html',context)