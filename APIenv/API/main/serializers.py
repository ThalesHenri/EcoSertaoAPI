from rest_framework import serializers
from .models import Fornecedor,Comprador,Produto
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class FornecedorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'cnpj', 'responsavel', 'cpfResponsavel' ,'password']

    def create(self,validated_data):
        fornecedor = Fornecedor(
            nome=validated_data['nome'],
            cnpj=validated_data['cnpj'],
            responsavel=validated_data['responsavel'],
            cpfResponsavel=validated_data['cpfResponsavel']
        )
        fornecedor.set_password(validated_data['password'])
        fornecedor.save()
        return fornecedor

class CompradorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Comprador
        fields = ['id','nome', 'cnpj', 'responsavel', 'cpfResponsavel', 'password']

    def create(self, validated_data):
        comprador = Comprador(
            nome=validated_data['nome'],
            cnpj=validated_data['cnpj'],
            responsavel=validated_data['responsavel'],
            cpfResponsavel=validated_data['cpfResponsavel']
        )
        comprador.set_password(validated_data['password'])
        comprador.save()
        return comprador

    
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'dataValid', 'marca', 'peso', 'quantidade', 'frete','preco', 'imagem']
        
        
