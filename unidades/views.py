from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Filial, Saldo
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
        hoje = datetime.now().date()
        #filial = Filial.objects.get(user = request.user)
        filial = Filial.objects.all()
        saldo = 5
        context = {'filial': filial, 'saldo': saldo}
        return render(request, 'home.html', context)



'''
#Comentar  ---->  CTRL + K e C
#Descomentar -->  CTRL + K e U
def home(request):
    if request.method == "GET":
        hoje = datetime.now().date()
        #filial = Filial.objects.get(user = request.user)
        filial = Filial.objects.all()
        print('==================================================================================')
        print(hoje)
        print('==================================================================================')
        print('==================================================================================')
        print(filial)
        print('==================================================================================')
        #saldo =  Saldo.objects.filter(filial__user = request.user).filter(data__gte = hoje).first
        saldo =  Saldo.objects.all() # .filter(data__gte = hoje).first
        print('==================================================================================')
        print(saldo)
        print('==================================================================================')
        if saldo:
            try:
                saldo = Saldo (data=datetime.now(), tergrasa=0, termasa=0, filial=filial.id)
                saldo.save()
                return redirect('/unidades/home')
            except:
                messages.add_message(request, constants.ERROR, 'Erro salvar data .')
                return redirect('/unidades/home')
        else:
            context = {'filial': filial, 'saldo': saldo}
            return render(request, 'home.html', context)
               
       
        
    


class Saldo(models.Model):
    data = models.DateField()
    tergrasa = models.IntegerField(default=0)
    termasa = models.IntegerField(default=0)
    filial = models.ForeignKey(Filial, on_delete=models.DO_NOTHING)

class Consulta(models.Model):

    paciente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_aberta = models.ForeignKey(DatasAbertas, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=status_choices, default='A')
    link = models.URLField(null=True, blank=True)

'''