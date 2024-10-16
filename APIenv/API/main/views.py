# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Usuario, Produto
from .serializers import UsuarioSerializer, ProdutoSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
import logging
from django.contrib.contenttypes.models import ContentType

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
        if isinstance(user, Usuario):
            user_data = {
                'nome': user.nome,
                'cnpj': user.cnpj,
                'responsavel': user.responsavel
                # Add other fields as necessary
            }
        else:
            logger.error("Unknown user type.")
            raise AuthenticationFailed('Unknown user type.')

        logger.info(f"User authenticated: {user_data}")
        return Response(user_data)
    
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        
        if not refresh_token:
            return Response({"detail": "Refresh token required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidToken as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    cnpj = request.data.get('cnpj')
    password = request.data.get('password')

    if not cnpj or not password:
        return Response({'error': 'CNPJ and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    user = None

    # Tentar buscar um Usuario
    try:
        user = Usuario.objects.get(cnpj=cnpj)
        if not user.check_password(password):
            return Response({'error': 'Invalid password for User'}, status=status.HTTP_401_UNAUTHORIZED)
        user_type = ContentType.objects.get_for_model(Usuario)
    except Usuario.edDoesNotExist:
        # Se não encontrar, tentar buscar um Usuario
        return Response({'error':'User cant be found'})
    # Criar um token usando o usuário encontrado
    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }, status=status.HTTP_200_OK)


    
@api_view(['GET', 'POST'])
def apiUsuariosLista(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = Usuario(
                nome=serializer.validated_data['nome'],
                cnpj=serializer.validated_data['cnpj'],
                responsavel=serializer.validated_data['responsavel'],
                cpfResponsavel=serializer.validated_data['cpfResponsavel']
            )
            usuario.set_password(serializer.validated_data['password'])
            usuario.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def apiUsuariosDetalhe(request, id):
    try:
        usuario = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario.delete()
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
