from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post

def index(request):
# query

    posts = Post.objects.all()
    context={
        'Title':'Blog',
        'Heading': 'Blog di mywebsite',
        'Posts':posts,
    }
    return render(request,'blog/index.html',context)

def categoryPost(request,categoryInput):
    post = Post.objects.filter(category=categoryInput)
    print(post)
    return HttpResponse("Category Post")
    
def singlePost(request, slugInput):
	post = Post.objects.get(slug=slugInput)
	context = {
		'test':'test'
	}
	judul = "<h1>{}</h1>".format(post.title)
	body = "<p>{}</p>".format(post.body)
	category = "<p>{}</p>".format(post.category)
	
	return HttpResponse(judul + body + category)