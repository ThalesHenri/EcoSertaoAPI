from django.db import models

# Create your models here.


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    responsavel = models.CharField(max_length=100, unique=True,default="SemValorInserido")
    cpfResponsavel = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return 'Fornecedor: ' + self.nome

class Comprador(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    responsavel = models.CharField(max_length=100, unique=True,default="SemValorInserido")
    cpfResponsavel = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return 'Comprador: ' + self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    dataValid = models.DateField(unique=True)
    marca = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2, unique=True)
    quantidade = models.IntegerField()
    opcao1 = 'CIF'
    opcao2 = 'FOB'
    opcaoEscolhas = [
        (opcao1,'CIF'),
        (opcao2,'FOB')
        ]
    frete = models.CharField(max_length=3,choices=opcaoEscolhas,default=opcao1)
    imagem = models.ImageField(upload_to='midia/')

    def __str__(self):
        return 'Produto: ' + self.nome