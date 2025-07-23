from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import generics
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer

# --- Views Principais ---

def home_view(request):
    """
    Renderiza a página inicial com o carrossel de mais vendidos.
    """
    produtos_mais_vendidos = Produto.objects.filter(is_mais_vendido=True)
    context = {
        'produtos': produtos_mais_vendidos,
    }
    return render(request, 'produtos/index.html', context)

def sobre_nos_view(request):
    """
    Renderiza a página 'Sobre Nós'.
    """
    return render(request, 'produtos/about_us.html')

def produto_detalhe_view(request, pk):
    """
    Mostra a página de detalhes de um único produto.
    """
    produto = get_object_or_404(Produto, pk=pk)
    context = {
        'produto': produto,
    }
    return render(request, 'produtos/produto_detalhe.html', context) # Corrigido de product_view.html


# --- Views de Categoria (COM PAGINAÇÃO) ---

def buques_view(request):
    try:
        categoria = Categoria.objects.get(nome__iexact="Buquês")
        lista_de_produtos = Produto.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        lista_de_produtos = []

    paginator = Paginator(lista_de_produtos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'titulo_da_pagina': 'Buquês'
    }
    return render(request, 'produtos/buque.html', context)

def presentes_view(request):
    try:
        categoria = Categoria.objects.get(nome__iexact="Presentes")
        lista_de_produtos = Produto.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        lista_de_produtos = []

    paginator = Paginator(lista_de_produtos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'titulo_da_pagina': 'Presentes'
    }
    return render(request, 'produtos/presente.html', context)

def jardinagem_view(request):
    try:
        categoria = Categoria.objects.get(nome__iexact="Jardinagem")
        lista_de_produtos = Produto.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        lista_de_produtos = []

    paginator = Paginator(lista_de_produtos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'titulo_da_pagina': 'Itens de Jardinagem'
    }
    return render(request, 'produtos/jardinagem.html', context)

def suculentas_view(request):
    try:
        categoria = Categoria.objects.get(nome__iexact="Suculentas")
        lista_de_produtos = Produto.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        lista_de_produtos = []

    paginator = Paginator(lista_de_produtos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'titulo_da_pagina': 'Suculentas'
    }
    return render(request, 'produtos/suculentas.html', context) # Corrigido de suculenta.html


# --- View de Busca (COM PAGINAÇÃO) ---

def search_view(request):
    query = request.GET.get('q', '')
    if query:
        lista_de_produtos = Produto.objects.filter(
            Q(nome__iexact=query) | Q(descricao__icontains=query)
        ).distinct()
    else:
        lista_de_produtos = []

    paginator = Paginator(lista_de_produtos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'titulo_da_pagina': f'Busca por "{query}"'
    }
    return render(request, 'produtos/search_results.html', context)


# --- Views da sua API (sem alterações) ---

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
    queryset = Produto.objects.filter(is_mais_vendido=True)
    serializer_class = ProdutoSerializer