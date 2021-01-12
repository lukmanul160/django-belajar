from django.urls import path

from . import views 

urlpatterns = [
    path('delete/<int:delete_id>', views.delete,name='delete'),
    path('update/<int:update_id>', views.update,name='update'),
    path('', views.list,name='list'),
    path('create/', views.create,name='create'),
]
