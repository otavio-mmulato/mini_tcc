from django.contrib import admin

from django.contrib import admin
from .models import Categoria, Produto

# Crie uma classe de admin para customizar a exibição dos produtos
class ProdutoAdmin(admin.ModelAdmin):
    # Campos que aparecerão na lista de produtos
    list_display = ('nome', 'preco', 'categoria', 'is_mais_vendido')
    
    # Adiciona um filtro na lateral para o campo 'is_mais_vendido'
    list_filter = ('is_mais_vendido', 'categoria')
    
    # Permite editar o campo 'is_mais_vendido' diretamente na lista
    list_editable = ('is_mais_vendido',)
    
    # Adiciona um campo de busca
    search_fields = ('nome', 'descricao')

# Registra os modelos no admin
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin) # Registra Produto usando a customização