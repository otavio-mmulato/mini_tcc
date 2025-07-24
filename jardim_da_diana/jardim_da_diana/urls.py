# Arquivo: jardim_da_diana/urls.py (O SEU ARQUIVO PRINCIPAL)
# VERSÃO CORRIGIDA E ORGANIZADA

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# --- CORREÇÃO AQUI ---
# 1. Importe APENAS as views que pertencem ao app 'produtos'
from produtos.views import (
home_view, 
buques_view, 
presentes_view, 
jardinagem_view, 
suculentas_view, 
sobre_nos_view, 
produto_detalhe_view, 
search_view
)
# As views de usuário (login, perfil, etc.) não são mais importadas aqui.
# Elas serão gerenciadas pelo 'include' abaixo.

urlpatterns = [
# Rota para o painel de administração
path('admin/', admin.site.urls),

# --- ROTAS DE PRODUTOS E PÁGINAS GERAIS ---
path('', home_view, name='home'),
path('buques/', buques_view, name='buques'),
path('presentes/', presentes_view, name='presentes'),
path('jardinagem/', jardinagem_view, name='jardinagem'),
path('suculentas/', suculentas_view, name='suculentas'),
path('sobre-nos/', sobre_nos_view, name='sobre-nos'),
path('produto/<int:pk>/', produto_detalhe_view, name='produto-detalhe'),
path('busca/', search_view, name='search'),

# --- ROTAS DE APPS SEPARADOS (MELHOR PRÁTICA) ---

# Delega TODAS as rotas de autenticação (login, cadastro, perfil, logout)
# para o arquivo 'urls.py' do app 'usuarios'.
# O prefixo '/auth/' será adicionado a todas as URLs de lá.
path('auth/', include('usuarios.urls')),

# Delega as rotas de API para o app 'produtos'
path('api/', include('produtos.urls')),

# Delega as rotas do carrinho para o app 'cart'
path('sacola/', include('cart.urls')),

path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticação do Django
]

# Configuração para servir arquivos de mídia em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)