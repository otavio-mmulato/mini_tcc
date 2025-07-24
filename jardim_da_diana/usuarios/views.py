from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# --- Views de Cadastro e Login ---

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        error_found = False
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já cadastrado.')
            error_found = True
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            error_found = True
        
        if error_found:
            return render(request, 'cadastro.html')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        messages.success(request, 'Conta criada com sucesso! Faça o login.')
        
        return redirect('/auth/login/') # Sugestão: use redirect('login') se sua URL de login tiver um nome

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(request, username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos, tente novamente.')
            return render(request, 'login.html')

# --- Views de Perfil e Logout (NOVO E NO LUGAR CERTO) ---

@login_required
def profile_view(request):
    """
    Exibe a página de perfil do usuário logado.
    """
    user = request.user
    context = {'user': user}
    # Renderiza o template 'perfil.html' que está em 'usuarios/templates/'
    return render(request, 'perfil.html', context)

def logout_view(request):
    """
    Faz o logout do usuário e redireciona para a página de login.
    """
    logout(request)
    return redirect('/auth/login/') # Sugestão: use redirect('login')