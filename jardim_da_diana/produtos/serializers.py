from rest_framework import serializers
from .models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only = True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset = Categoria.objects, source = 'categoria', write_only = True) # permite receber o ID da categoria ao criar ou atualizar um produto
    
    class Meta:
        model = Produto
        fields = '__all__'
