from django.shortcuts import render
from django.views import View



def index(request):
    context= {
        'heading':'SELAMAT DATANG'
    }
    if request.method == 'POST':
        context['heading'] = 'Post Function Base View'
    return render(request,'index.html',context)


class IndexClassView(View):
    # override method get dari parent class View

    template_name = 'index.html'
    context = {
    }

    def get(self,request):
        self. context['heading'] = 'GET class Base View'
        return render(request,self.template_name,self.context)

    def post(self,request):
        self. context['heading'] = 'Post class Base View'
        return render(request,self.template_name,self.context)