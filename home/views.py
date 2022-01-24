from email import message
from msilib.schema import ListView
from django.shortcuts import render
from .models import Contato
from django.http import HttpResponse


def index(request):
   return render(request, "pages/index.html")


def contato(request):
   if request.method=="POST":
      contato=Contato()
      nome=request.POST.get('name')
      sobrenome=request.POST.get('sobrenome')
      email=request.POST.get('email')
      message=request.POST.get('message')
      contato.nome=nome
      contato.sobrenome=sobrenome
      contato.email=email
      contato.message=message
      contato.save()
      return HttpResponse("<h1>Obrigado por entrar em contato</h1>")
   return render(request, "pages/contato.html")    

