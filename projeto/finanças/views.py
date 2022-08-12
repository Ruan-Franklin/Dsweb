from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Views da página de finanças.
def index(request):
    return HttpResponse("Bem-vindo á primeira View de finanças!")