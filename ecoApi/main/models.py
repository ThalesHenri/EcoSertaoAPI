from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom User Manager for handling user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, cnpj, password=None, **extra_fields):
        if not cnpj:
            raise ValueError('The CNPJ field must be set')
        user = self.model(cnpj=cnpj, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cnpj, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(cnpj, password, **extra_fields)

class Usuario(AbstractBaseUser):
    cnpj = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100, default="SemValorInserido")
    cpfResponsavel = models.CharField(max_length=30)
    password = models.CharField(max_length=128, default=make_password('senha123'))
    is_active = models.BooleanField(default=True)
    
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'cnpj'
    REQUIRED_FIELDS = ['nome', 'responsavel', 'cpfResponsavel']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return 'Usuario: ' + self.nome



class Produto(models.Model):
    nome = models.CharField(max_length=100)
    dataValid = models.DateField()
    marca = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    opcao1 = 'CIF'
    opcao2 = 'FOB'
    opcaoEscolhas = [
        (opcao1, 'CIF'),
        (opcao2, 'FOB')
    ]
    frete = models.CharField(max_length=3, choices=opcaoEscolhas, default=opcao1)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagem = models.ImageField(upload_to='midia/')

    def __str__(self):
        return 'Produto: ' + self.nome

