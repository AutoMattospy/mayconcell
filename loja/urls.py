# loja/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name='produtos'),
    path('servicos/', views.servicos, name='servicos'),
    path('produto/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
]