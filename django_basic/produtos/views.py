from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def ver_produto(request):
    if request.method == "GET":
        nome = "Gustavo"
        return render(request, 'ver_produto.html', {'nome': nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        
        #Salvar informações no banco
        #pessoa = Pessoa(nome=nome, idade=idade)

        #pessoa.save()

        #Retornar informações do banco
        #Todas
        #pessoas = Pessoa.objects.all()
        #Com filtro
        pessoas = Pessoa.objects.filter(nome=nome)
        print(pessoas)

        return HttpResponse(pessoas)

def inserir_produto(request):
    return HttpResponse('Inserir produto')