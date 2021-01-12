from django.shortcuts import render,redirect

# Create your views here.
from .forms import PostForm
from .models import Post

def index(request):

    posts = Post.objects.all()
    context = {
        'post_title':'CREATE POST',
        'posts':posts
    }
    return render(request,'blog/index.html',context)

def create(request):
    post_form = PostForm(request.POST or None)

    if request.method =="POST":
        if post_form.is_valid():
            # Post.objects.create(
            #     judul       = request.POST.get('judul'),
            #     body        = request.POST.get('body'),
            #     category   = request.POST.get('category') ,
            # )
            post_form.save()

            return redirect('blog:index')

    context = {
        'post_title':'CREATE POST',
        'post_form':post_form
    }
    return render(request,'blog/create.html',context)