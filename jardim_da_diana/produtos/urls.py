# produtos/urls.py

from django.urls import path
from . import views

# Estas são apenas as rotas DENTRO de /api/
urlpatterns = [
    path('categorias/', views.CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    path('produtos/', views.ProdutoList.as_view(), name='produto-list'),
    path('produtos/<int:pk>/', views.ProdutoDetail.as_view(), name='produto-detail'),
    path('produtos/mais-vendidos/', views.MaisVendidosList.as_view(), name='mais-vendidos-list'),
]