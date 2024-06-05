from django.db import models

# Create your models here.


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return 'Fornecedor: ' + self.nome

class Comprador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return 'Comprador: ' + self.nome