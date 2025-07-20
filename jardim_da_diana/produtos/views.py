# produtos/views.py

from django.shortcuts import render
from rest_framework import generics
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer
from django.shortcuts import render, get_object_or_404
# --- View para a Página Principal ---
def home_view(request):
    """
    Esta view renderiza o template da página inicial, passando os
    produtos marcados como 'mais vendido' para o carrossel.
    """
    produtos_mais_vendidos = Produto.objects.filter(is_mais_vendido=True)
    context = {
        'produtos': produtos_mais_vendidos,
    }
    return render(request, 'produtos/index.html', context)


# --- Views da sua API (continuam aqui para uso futuro) ---
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class MaisVendidosList(generics.ListAPIView):
    """
    API endpoint que retorna uma lista de produtos
    marcados como 'mais vendido'.
    """
    queryset = Produto.objects.filter(is_mais_vendido=True)
    serializer_class = ProdutoSerializer

def buques_view(request):
    try:
        categoria_buques = Categoria.objects.get(nome__iexact="Buquês")
        produtos_da_categoria = Produto.objects.filter(categoria=categoria_buques)
    except Categoria.DoesNotExist:
        produtos_da_categoria = []
    
    context = {
        'produtos': produtos_da_categoria,
        'titulo_da_pagina': 'Buquês'
    }
    return render(request, 'produtos/buque.html', context)

def presentes_view(request):
    try:
        categoria_presentes = Categoria.objects.get(nome__iexact="Presentes")
        produtos_da_categoria = Produto.objects.filter(categoria=categoria_presentes)
    except Categoria.DoesNotExist:
        produtos_da_categoria = []
    
    context = {
        'produtos': produtos_da_categoria,
        'titulo_da_pagina': 'Presentes'
    }
    return render(request, 'produtos/presente.html', context)

def jardinagem_view(request):
    try:
        categoria_jardinagem = Categoria.objects.get(nome__iexact="Jardinagem")
        produtos_da_categoria = Produto.objects.filter(categoria=categoria_jardinagem)
    except Categoria.DoesNotExist:
        produtos_da_categoria = []
    
    context = {
        'produtos': produtos_da_categoria,
        'titulo_da_pagina': 'Jardinagem'
    }
    return render(request, 'produtos/jardinagem.html', context)

def suculentas_view(request):
    try:
        categoria_suculentas = Categoria.objects.get(nome__iexact="Suculentas")
        produtos_da_categoria = Produto.objects.filter(categoria=categoria_suculentas)
    except Categoria.DoesNotExist:
        produtos_da_categoria = []
    
    context = {
        'produtos': produtos_da_categoria,
        'titulo_da_pagina': 'Suculentas'
    }
    return render(request, 'produtos/suculenta.html', context)

def sobre_nos_view(request):
    return render(request, 'produtos/about_us.html')

def produto_detalhe_view(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    context = {
        'produto': produto,
    }
    return render(request, 'produtos/product_view.html', context)