from django.db import models

# Create your models here.
class Regiao(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.nome)
    
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=15)
    site = models.CharField(max_length=100)
    coleta = models.BooleanField()
    descarte = models.BooleanField()

    regiao = models.ForeignKey(Regiao, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({} , {})".format(self.regiao.nome, self.nome, self.cep)