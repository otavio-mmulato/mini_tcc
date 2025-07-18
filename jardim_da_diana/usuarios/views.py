from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages # NOVO: Importa o framework de mensagens

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        # ALTERADO: Lógica de verificação de erros
        error_found = False
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já cadastrado.')
            error_found = True
        
        # NOVO: Verificação de e-mail existente
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            error_found = True
        
        if error_found:
            # Se encontrou qualquer erro, renderiza a página de novo para mostrar as mensagens
            return render(request, 'cadastro.html')

        # Se passou por todas as verificações, cria o usuário
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        # NOVO: Mensagem de sucesso
        messages.success(request, 'Conta criada com sucesso! Faça o login.')
        
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
            # Dica: É uma boa prática usar name na sua URL e redirecionar com redirect('nome_da_url')
            return redirect('/plataforma/') # Alterei para a página da plataforma
        else:
            # ALTERADO: Usa o messages para enviar o erro
            messages.error(request, 'Nome de usuário ou senha incorretos, tente novamente.')
            return render(request, 'login.html')

def logout_view(request):   
    logout(request)
    return redirect('/auth/login/')

@login_required(login_url='/auth/login/')
def plataforma(request):
    return render(request, 'plataforma.html')