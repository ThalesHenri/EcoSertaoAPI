# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Fornecedor, Comprador, Produto
from .serializers import FornecedorSerializer, CompradorSerializer, ProdutoSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
import logging

logger = logging.getLogger(__name__)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"message": "This is a protected view!"}, status=200)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            logger.warning("User not authenticated.")
            raise AuthenticationFailed('Authentication credentials were not provided.')
        
        # Check the type of user and fetch data accordingly
        if isinstance(user, Fornecedor):
            user_data = {
                'nome': user.nome,
                'cnpj': user.cnpj,
                # Add other fields as necessary
            }
        elif isinstance(user, Comprador):
            user_data = {
                'nome': user.nome,
                'cnpj': user.cnpj,
                # Add other fields as necessary
            }
        else:
            logger.error("Unknown user type.")
            raise AuthenticationFailed('Unknown user type.')

        logger.info(f"User authenticated: {user_data}")
        return Response(user_data)
    
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
def login(request):
    cnpj = request.data.get('cnpj')
    password = request.data.get('password')

    if not cnpj or not password:
        return Response({'error': 'CNPJ and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    # Check against Fornecedor and Comprador models
    try:
        user = Fornecedor.objects.get(cnpj=cnpj)
        if not user.check_password(password):
            raise Fornecedor.DoesNotExist
    except Fornecedor.DoesNotExist:
        try:
            user = Comprador.objects.get(cnpj=cnpj)
            if not user.check_password(password):
                raise Comprador.DoesNotExist
        except Comprador.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })

@api_view(['GET', 'POST'])
def apiFornecedoresLista(request):
    if request.method == 'GET':
        fornecedor = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedor, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            fornecedor = Fornecedor(
                nome=serializer.validated_data['nome'],
                cnpj=serializer.validated_data['cnpj'],
                responsavel=serializer.validated_data['responsavel'],
                cpfResponsavel=serializer.validated_data['cpfResponsavel']
            )
            fornecedor.set_password(serializer.validated_data['password'])
            fornecedor.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def apiCompradoresLista(request):
    if request.method == 'GET':
        comprador = Comprador.objects.all()
        serializer = CompradorSerializer(comprador, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = CompradorSerializer(data=request.data)
        if serializer.is_valid():
            comprador = Comprador(
                nome=serializer.validated_data['nome'],
                cnpj=serializer.validated_data['cnpj'],
                responsavel=serializer.validated_data['responsavel'],
                cpfResponsavel=serializer.validated_data['cpfResponsavel']
            )
            comprador.set_password(serializer.validated_data['password'])
            comprador.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def apiFornecedoresDetalhe(request, id):
    try:
        fornecedor = Fornecedor.objects.get(pk=id)
    except Fornecedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def apiCompradoresDetalhe(request, id):
    try:
        comprador = Comprador.objects.get(pk=id)
    except Comprador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompradorSerializer(comprador)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompradorSerializer(comprador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comprador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def apiProdutolista(request):
    if request.method == 'GET':
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def apiProdutosDetalhe(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Produto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
