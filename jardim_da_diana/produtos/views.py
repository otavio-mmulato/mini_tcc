# produtos/views.py

from django.shortcuts import render
from rest_framework import generics
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer

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