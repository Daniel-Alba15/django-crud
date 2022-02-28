from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autores/', views.listarAutores, name='autores'),
    path('autores/new', views.create_autor, name='new_autor'),
    path('autores/<id>/', views.detail_view, name='autor_detail'),
    path('autores/update/<id>/', views.update_autor, name='autor_update'),
    path('autores/delete/<id>/', views.delete_view, name='autor_delete'),
    path('libros/', views.listar_libros, name='libros'),
    path('libros/new', views.create_book, name='new_book'),
    path('libros/update/<id>/', views.update_book, name='update_book'),
    path('libros/<id>/', views.book_detail, name='book_detail'),
    path('libros/delete/<id>/', views.delete_book, name='delete_book'),

]