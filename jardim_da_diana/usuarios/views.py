from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=username).exists():
            return render(request, 'cadastro.html', {'erro': 'Já existe um usuário com esse username.'})

        User.objects.create_user(username=username, email=email, password=senha)
        return redirect('/auth/login/')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(request, username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('/static/frontend/index.html')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos.'})

def logout_view(request):   
    logout(request)
    return redirect('/auth/login/')

@login_required(login_url='/auth/login/')
def plataforma(request):
    return render(request, 'plataforma.html')
