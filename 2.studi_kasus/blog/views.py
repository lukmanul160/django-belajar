from django.shortcuts import render

from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'Judul':'Home Blog',
        'Content':'ini adalah halaman blog',
        'Posts':posts,
        'Categories':categories,
    }
    return render(request,'blog/index.html',context)

def detailPost(request,slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'Judul':'Home Blog',
        'Content':'ini adalah halaman blog',
        'Posts':posts,
        'Categories':categories,
    }
    return render(request,'blog/detail.html',context)

def categoryPost(request,categoryInput):
    posts = Post.objects.filter(category=categoryInput)
    categories = Post.objects.values('category').distinct()
    print(posts)
    context = {
        'Judul':'Home Blog',
        'Content':'Tampilkan berdasarkan Kategori',
        'Posts':posts,
        'Categories':categories,
    }
    return render(request,'blog/category.html',context)