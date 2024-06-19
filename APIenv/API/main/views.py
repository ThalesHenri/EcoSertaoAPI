from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Fornecedor,Comprador
from .serializers import FornecedorSerializer,CompradorSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def apiFornecedoresLista(request):
    
    if request.method == 'GET':
        #retorna a lista completa de fornecedores
        fornecedor = Fornecedor.objects.all()
        serializer  = FornecedorSerializer(fornecedor, many=True)
        return JsonResponse(serializer.data, safe=False)
        #pegar as informaçoes dos fornecedores no banco de dados
        #transformar em json
        #enviar via JsonResponse
    elif request.method == 'POST':
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET','POST'])
def apiCompradoresLista(request):
    
    if request.method == 'GET':
        comprador = Comprador.objects.all()
        serializer = CompradorSerializer(comprador, many=True)
        
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = CompradorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def apiFornecedoresDetalhe(request,id):
    
    try:
        fornecedor = Fornecedor.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': #recebe
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)
    elif request.method == 'PUT': #atualiza
        serializer = FornecedorSerializer(fornecedor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': #apaga IMPORTANTE: preciso restringir o acesso deste metodo
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT','DELETE'])
def apiCompradoresDetalhe(request,id):
    
    try:
        comprador = Comprador.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CompradorSerializer(comprador)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompradorSerializer(comprador,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comprador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
        