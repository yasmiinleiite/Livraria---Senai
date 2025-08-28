from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor, Editora, Livro
from .serializers import AutorSerializer, EditoraSerializar, LivroSerializer
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_autores(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
############### Autores ###############
class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAuthenticated]
    
class AutoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

########################################

#$$$$$$$$$$$$$$$$ Editoras $$$$$$$$$$$$$
class EditorasView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializar
    permission_classes = [IsAuthenticated]



class EditorasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializar
    permission_classes = [IsAuthenticated]


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#%%%%%%%%%%%%%% Livros %%%%%%%%%%%%%%%%%

class LivroView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer 
    permission_classes = [IsAuthenticated]

class LivroDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer 
    permission_classes = [IsAuthenticated]

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    