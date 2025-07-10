from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('plataforma', views.plataforma, name='plataforma'),
    path('logout/', logout_view, name='logout'),
]