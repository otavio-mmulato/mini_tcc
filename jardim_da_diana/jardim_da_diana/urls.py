# jardim_da_diana/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from produtos.views import home_view, buques_view, presentes_view, jardinagem_view, suculentas_view, sobre_nos_view, produto_detalhe_view, search_view # Importa a view da sua página inicial

urlpatterns = [
    # Rota para o painel de administração
    path('admin/', admin.site.urls),

    # Rota para a sua página inicial (a raiz do site)
    path('', home_view, name='home'),

    # Delega as rotas de API para o app 'produtos'
    path('api/', include('produtos.urls')),

    # Delega as rotas de autenticação para o app 'usuarios'
    path('auth/', include('usuarios.urls')),

    path('busca/', search_view, name='search'),

    path('sacola/', include('cart.urls')),  # Rota para o carrinho de compras

    path('buques/', buques_view, name='buques'),  # Rota para a página de buquês

    path('presentes/', presentes_view, name='presentes'),  # Rota para a página de presentes

    path('jardinagem/', jardinagem_view, name='jardinagem'),  # Rota para a página de jardinagem
    
    path('suculentas/', suculentas_view, name='suculentas'),

    path('sobre-nos/', sobre_nos_view, name='sobre-nos'),  # Rota para a página "Sobre Nós"

    path('produto/<int:pk>/', produto_detalhe_view, name='produto-detalhe')
]

# Configuração para servir arquivos de mídia (imagens dos produtos)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)