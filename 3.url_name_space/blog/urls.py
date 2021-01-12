from django.urls import path,re_path

from . import views


urlpatterns = [
    path('khusus/<slug:input>',views.khususPost,name="khusus"),
    path('category/',views.categoryPost,name='category'),
    path('singel/',views.singelPost, name="single"),
    path('',views.index,name="index"),   
]
