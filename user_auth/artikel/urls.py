from django.urls import path

from .views import artikelIndexView, otongView, artikelAddView, artikelAddView2

urlpatterns = [
    path('', artikelIndexView, name='index'),
    path('martin', otongView, name='martin'),
    path('add2', artikelAddView2, name='add2'),
    path('add', artikelAddView, name='add'),
]
