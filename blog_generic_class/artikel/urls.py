from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from .views import ArtikelListView,ArtikelDetailView,ArtikelKategoriListView,ArtikelCreateView,ArtikelDeleteView,ArtikelUpdateView,ArtikelManageView

urlpatterns = [
    path('manage/update/<slug:pk>', ArtikelUpdateView.as_view(), name='update'),
	path('manage/delete/<slug:pk>', ArtikelDeleteView.as_view(), name='delete'),
	path('manage/', ArtikelManageView.as_view(), name='manage'),
    path('tambah/', ArtikelCreateView.as_view(), name='create'),
    path('detail/<slug:slug>',ArtikelDetailView.as_view(),name='detail'),
    path('kategory/<slug:kategori>/<int:page>',ArtikelKategoriListView.as_view(),name='category'),
    path('<int:page>',ArtikelListView.as_view(),name='list')
]
