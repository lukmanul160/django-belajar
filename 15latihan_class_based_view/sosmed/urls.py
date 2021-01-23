from django.urls import path

from .views import (
    SosmedListView,
    SosmedDeleteView,
    SosmedFormView)

urlpatterns = [
    path('delete/<int:delete_id>', SosmedDeleteView.as_view(),name='delete'),
    path('', SosmedListView.as_view(),name='list'),
        path('update/<int:update_id>', SosmedFormView.as_view(mode='update'),name='update'),
    path('create/', SosmedFormView.as_view(mode='create'),name='create'),
]
