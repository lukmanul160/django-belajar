from django.shortcuts import render

from . forms import ContactForm
# Create your views here.
def index(request):
    contact_form = ContactForm()
    context = {
        'heading':'Contact',
        'data_form':contact_form
    }

    print(request.POST)

    return render(request,'index.html',context)