from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
#vai criar um numero sequancial n duplicavel que vai representar unicamente o meu usuario 
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
