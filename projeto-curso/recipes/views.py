from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name':'Gustavo'
    })

def about(request):
    return HttpResponse('Sobre')

def contact(request):
    return render(request, 'recipes/contact.html')