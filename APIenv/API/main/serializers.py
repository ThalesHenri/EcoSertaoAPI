from rest_framework import serializers
from .models import Fornecedor,Comprador

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'cnpj', 'email', 'telefone' ]


class CompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprador
        fields = ['id','nome','cpf','email','telefone']