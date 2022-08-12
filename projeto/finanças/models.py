from django.db import models
#Signals serve para enviar alguma notificação a outro modelo quando determinado evento ocorrer.
from django.db.models.signals import post_save
#

class Cliente(models.Model):
    nome=models.CharField(max_length=200)
    gasto=models.FloatField()
    ultima_movimentacao=models.DateTimeField(auto_now=True)
    def get_ultima_movimentacao(self):
           return self.ultima_movimentacao.strftime('%d/%m/%Y %H:%M')



# Create your models here.
