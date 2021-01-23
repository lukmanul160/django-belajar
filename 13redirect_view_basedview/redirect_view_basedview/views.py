from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404

class HomeViews(RedirectView):
    # url = '/'
    pattern_name='index'

class HomeRedirectView(RedirectView):
    patter_name="index"

    permanent = False
    query_string = True

        