from django.shortcuts import render

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    pass
 
class ContextView(TemplateView):
    template_name = 'context.html'

    def get_context_data(self):
        context = {
            'judul':'HOME CONTEXT',
            'penulis':'ujang' 
        }

        return context

class PrameterView(TemplateView):
    template_name = 'parameter.html'

    def get_context_data(self,*args, **kwargs):
        context = kwargs
        context['judul'] = 'Home Parameter'
        context['penulis'] = 'ujang'
        return context
    

    

    

