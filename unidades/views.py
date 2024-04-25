from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Filial
from django.contrib.messages import constants
from django.contrib import messages


#@login_required
def cadastro_filial(request):

    if request.method == "GET":
        
        context = {}
        return render(request, 'cadastro_filial.html', context )
    elif request.method == "POST":
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cidade = request.POST.get('cidade')
        cpf = request.FILES.get('cpf')
        foto = request.FILES.get('foto')
        try:
            dados_filial = Filial(nome=nome, cep=cep, rua=rua, bairro=bairro, numero=numero, 
                                  cidade=cidade, cpf=cpf, foto=foto, user=request.user,)
            dados_filial.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro da Filial realizado com sucesso.')
            return redirect('/usuarios/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro ao salvar Medico.')
            return redirect('/unidades/cadastro_filial')


#Comentar  ---->  CTRL + K e C
#Descomentar -->  CTRL + K e U
def home(request):
    if request.method == "GET":
        filial = 'nnn' #Filial.objects.get (user = request.user)
       
        context = {'filial': filial}
        return render(request, 'home.html', context)