from rest_framework import serializers
from .models import Fornecedor,Comprador,Produto

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'cnpj', 'responsavel', 'cpfResponsavel' ]


class CompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprador
        fields = ['id', 'nome', 'cnpj', 'responsavel', 'cpfResponsavel' ]
    
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'dataValid', 'marca', 'peso', 'quantidade', 'frete','preco', 'imagem']