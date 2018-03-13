from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.usuario


class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=12)

    def __str__(self):
        return self.cpf


class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=18)
    razaosocial = models.CharField(max_length=100)

    def __str__(self):
        return self.cnpj


class Autor(Pessoa):
    curriculo = models.CharField(max_length=200)
    artigos = models.CharField(max_length=100)

    def __str__(self):
        return self.curriculo


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    sigla = models.CharField(max_length=10)
    numero = models.IntegerField(max_length=10)
    realizador = models.ManyToOneRel(PessoaFisica, on_delete=models.CASCADE,field_name=PessoaFisica, to=nome)
    logo = models.CharField(max_length=10)
    data_de_inicio = models.DateField(max_length=10)
    data_de_fim = models.DateField(max_length=10)

    def __str__(self):
        return self.nome


class EventoCientifico(Evento):
    issn = models.CharField(max_length=100)

    def __str__(self):
        return self.issn


class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=150)
    autores = models.CharField(max_length=250)
    evento = models.ManyToOneRel(EventoCientifico, on_delete=models.CASCADE, field_name=EventoCientifico, to=Evento.nome)
