from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import generics
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer

# --- Views Principais ---

def home_view(request):
    produtos_mais_vendidos = Produto.objects.filter(is_mais_vendido=True)
    context = { 'produtos': produtos_mais_vendidos, }
    return render(request, 'produtos/index.html', context)

def sobre_nos_view(request):
    return render(request, 'produtos/about_us.html')

def produto_detalhe_view(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    context = { 'produto': produto, }
    return render(request, 'produtos/product_view.html', context)


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
    context = { 'page_obj': page_obj, 'titulo_da_pagina': 'Buquês' }
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
    context = { 'page_obj': page_obj, 'titulo_da_pagina': 'Presentes' }
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
    context = { 'page_obj': page_obj, 'titulo_da_pagina': 'Itens de Jardinagem' }
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
    context = { 'page_obj': page_obj, 'titulo_da_pagina': 'Suculentas' }
    return render(request, 'produtos/suculentas.html', context)


# --- View de Busca (COM PAGINAÇÃO E CORREÇÃO) ---

def search_view(request):
    query = request.GET.get('q', '')
    if query:
        # CORREÇÃO AQUI: trocamos __iexact por __icontains
        lista_de_produtos = Produto.objects.filter(
            Q(nome__icontains=query) | Q(descricao__icontains=query)
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

class MaisVendidosList(generics.ListCreateAPIView):
    queryset = Produto.objects.filter(is_mais_vendido=True)
    serializer_class = ProdutoSerializer