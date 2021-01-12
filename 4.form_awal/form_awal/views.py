from django.shortcuts import render

def index(request):
    context = {
        'heading':'HOME'
    }
    if request.method == 'POST':
        print('metod post')
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
        
    else:
        print('metod get')
    return render(request,'index.html',context)