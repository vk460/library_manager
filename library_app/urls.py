# library_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.book_create, name='book_add'),
    path('edit/<int:pk>/', views.book_update, name='book_edit'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]
