from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')
        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Ja existe um usuario com este username.')
            return redirect('/usuarios/cadastro')
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'A senha e o confirmar senha tem que ser iguais')
            return redirect('/usuarios/cadastro')
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha tem que ter mais de 6 digitos.')
            return redirect('/usuarios/cadastro')
        
        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            return redirect('/usuarios/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro ao salvar o Usuario.')
            return redirect('/usuarios/cadastro')
        
def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')   
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get("senha")
        user = auth.authenticate(request, username=username, password=senha) 

        if user:
            auth.login(request, user)
            return redirect('/unidades/home')
        
        messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/usuarios/login')
    
def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login')
            