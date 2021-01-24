from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
# Create your views here.
@permission_required('blog.add_artikel',login_url=None,raise_exception=True)
# @permission_required('blog.add_artikel',login_url='/admin/')
def addView(request):
    context = {
        'page:title':'Add Artikel'
    }
    return render(request,'blog/add.html',context)


@permission_required('blog.can_edit')
def updateView(request):
    context = {
        'page:title':'Blog'
    }

    return render(request,'blog/edit.html',context)



def indexView(request):
    print(request.user.get_all_permissions())
    context = {
        'page:title':'Blog'
    }

    return render(request,'blog/index.html',context)