# jardim_da_diana/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from produtos.views import home_view # Importa a view da sua página inicial

urlpatterns = [
    # Rota para o painel de administração
    path('admin/', admin.site.urls),

    # Rota para a sua página inicial (a raiz do site)
    path('', home_view, name='home'),

    # Delega as rotas de API para o app 'produtos'
    path('api/', include('produtos.urls')),

    # Delega as rotas de autenticação para o app 'usuarios'
    path('auth/', include('usuarios.urls')),
]

# Configuração para servir arquivos de mídia (imagens dos produtos)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)