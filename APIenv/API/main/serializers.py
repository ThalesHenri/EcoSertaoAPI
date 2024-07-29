# serializers.py
from rest_framework import serializers
from .models import Fornecedor, Comprador, Produto
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

class FornecedorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'cnpj', 'responsavel', 'cpfResponsavel', 'password']

    def create(self, validated_data):
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
        fields = ['id', 'nome', 'cnpj', 'responsavel', 'cpfResponsavel', 'password']

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
        fields = ['id', 'nome', 'dataValid', 'marca', 'peso', 'quantidade', 'frete', 'preco', 'imagem']

class CustomTokenObtainPairSerializer(serializers.Serializer):
    cnpj = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        return RefreshToken.for_user(obj).access_token

    def validate(self, attrs):
        cnpj = attrs.get('cnpj')
        password = attrs.get('password')

        try:
            user = Fornecedor.objects.get(cnpj=cnpj)
            if not check_password(password, user.password):
                raise serializers.ValidationError('Incorrect credentials')
        except Fornecedor.DoesNotExist:
            try:
                user = Comprador.objects.get(cnpj=cnpj)
                if not check_password(password, user.password):
                    raise serializers.ValidationError('Incorrect credentials')
            except Comprador.DoesNotExist:
                raise serializers.ValidationError('Incorrect credentials')

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
