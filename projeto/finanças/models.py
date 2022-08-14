from django.db import models
from django.contrib.auth.models import User
#Signals serve para enviar alguma notificação a outro modelo quando determinado evento ocorrer.
#from django.db.models.signals import post_save
#

class Cliente(models.Model):
    nome=models.CharField(max_length=200)
    foto=models.ImageField(upload_to = 'Clientes',null=True, blank = True)
    gasto=models.DecimalField(max_digits=10,decimal_places=2)
    #str para retornar a representação de uma string como objeto
    #Com self conseguimos acessar atributos e métodos de uma classe  em Python
    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name_plural="Clientes"
    


# Create your models here.
