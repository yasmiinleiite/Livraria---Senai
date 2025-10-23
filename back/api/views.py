from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Autor, Editora, Livro, Imagem
from .serializers import AutorSerializer, EditoraSerializer, LivroSerializer, RegisterSerializer, ImagemSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from .filters import AutorFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET', 'POST'])
def listar_autores(request):
    if request.method=='GET':
        queryset = Autor.objects.all()
        serializers = AutorSerializer(queryset, many=True)
        return Response(serializers.data)
    elif request.method=='POST':
        serializers = AutorSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    # permission_classes =[IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['id']               # Permite o filtro exato
    # search_fields = ['nome', 'sobrenome']   # busca parcial: ?search=Jorge
    filterset_class = AutorFilter           # Caso queira filtro duplo "Nome" e "Nacionalidade"
    
class AutoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes =[IsAuthenticated]

class EditorasView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    # permission_classes =[IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'nome']
    search_fields = ['nome']  

class EditorasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    permission_classes =[IsAuthenticated]

class LivrosView(ListCreateAPIView):
    queryset = Livro.objects.all().select_related('autor')
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['titulo', 'autor__nome', 'autor__sobrenome']
    ordering_fields = ['id', 'titulo']
    ordering = ['titulo']


class LivrosDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    # permission_classes =[IsAuthenticated]

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all().select_related('autor')
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # se você criou o LivroFilter com autor/titulo:
    search_fields = ['titulo', 'autor__nome', 'autor__sobrenome']
    ordering_fields = ['id', 'titulo']
    ordering = ['titulo']

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': {'id': user.id, 'username': user.username},
            'tokens': {'refresh': str(refresh), 'access': str(refresh.access_token)}
        }, status=status.HTTP_201_CREATED)
            
class ImagemViewSet(ModelViewSet):
    queryset = Imagem.objects.all().order_by("-criado_em")
    serializer_class = ImagemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Livro
from .serializers import LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.select_related("autor").order_by("-id")
    serializer_class = LivroSerializer
    parser_classes = [MultiPartParser, FormParser]

    # filtros / busca / ordenação
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["titulo", "autor__nome", "autor__sobrenome"]
    ordering_fields = ["id", "titulo"]
    ordering = ["titulo"]

    @action(detail=True, methods=["post"], parser_classes=[MultiPartParser, FormParser])
    def capa(self, request, pk=None):
        """
        POST /api/livros/{id}/capa/
        FormData: campo 'capa' (arquivo)
        """
        livro = self.get_object()
        arquivo = request.FILES.get("capa")
        if not arquivo:
            return Response(
                {"detail": "Arquivo 'capa' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        livro.capa = arquivo
        livro.save(update_fields=["capa"])
        return Response(self.get_serializer(livro).data, status=status.HTTP_200_OK)
