from django.db import models

# Create your models here.

class Pessoa(models.Model): #Modelo de exemplo. É similar a agenda do google
    nome = models.CharField(max_length=128)
    telefone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField()
    criador = models.ForeignKey('auth.user', related_name='pessoas', on_delete=models.CASCADE)

    def save(self, *args,**kwargs):
        super(Pessoa,self).save(*args, **kwargs)
