from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    responsavel = models.CharField(max_length=100, unique=True,default="SemValorInserido")
    cpfResponsavel = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128,default=make_password('senha123'))

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    
    def __str__(self):
        return 'Fornecedor: ' + self.nome

class Comprador(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    responsavel = models.CharField(max_length=100, unique=True,default="SemValorInserido")
    cpfResponsavel = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128,default=make_password('senha123'))

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    
    def __str__(self):
        return 'Comprador: ' + self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    dataValid = models.DateField()
    marca = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    opcao1 = 'CIF'
    opcao2 = 'FOB'
    opcaoEscolhas = [
        (opcao1,'CIF'),
        (opcao2,'FOB')
        ]
    frete = models.CharField(max_length=3,choices=opcaoEscolhas,default=opcao1)
    preco = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    imagem = models.ImageField(upload_to='midia/')

    def __str__(self):
        return 'Produto: ' + self.nome
    
