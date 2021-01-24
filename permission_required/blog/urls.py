from django.urls import path

from.views import addView,indexView,updateView

urlpatterns = [
    path('',indexView,name='index'),
    path('add',addView,name='add'),
    path('update',updateView,name='update'),
]
