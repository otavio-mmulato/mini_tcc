from django.urls import path
from . import views
from .views import logout_view, profile_view

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', profile_view, name='perfil'),
    path('logout/', logout_view, name='logout'),
]