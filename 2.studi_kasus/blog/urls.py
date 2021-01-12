from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    re_path('post/(?P<slugInput>[\w-]+)/$',views.detailPost,name="detail"),
    re_path('category/(?P<categoryInput>[\w-]+)/$',views.categoryPost,name="category"),
]
