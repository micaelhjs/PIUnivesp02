from django.db import models
from django.contrib.auth.models import User

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
        return "{} ({} , {} , {} )".format(self.nome, self.regiao.nome, self.endereco,self.bairro)
    
class AgendamentoColeta(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=500, verbose_name="Descrição")
    local = models.CharField(max_length=255, verbose_name="Endereço da Coleta")

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({} , {})".format(self.empresa.nome, self.data, self.hora)
    
class AgendamentoDescarte(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=500, verbose_name="Descrição")

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({} , {})".format(self.empresa.nome, self.data, self.hora)