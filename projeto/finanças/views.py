from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from django.urls import reverse

# Create your views here.
#Views da página de finanças.
class PrincipalView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'templates/dash.html')

def index(request):
    return HttpResponse("Bem-vindo á primeira View de finanças!")