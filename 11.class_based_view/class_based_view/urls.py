
from django.contrib import admin
from django.urls import path

from .views import index,IndexClassView

urlpatterns = [
    path('', index,name='index'),
    path('class',IndexClassView.as_view(),name='home-class'),
    path('admin/', admin.site.urls),
]
