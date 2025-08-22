from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor, Editora, Livro
from .serializers import AutorSerializer, EditoraSerializar, LivroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


    
@api_view(['GET', 'POST'])
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
    
class AutoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

########################################

#$$$$$$$$$$$$$$$$ Editoras $$$$$$$$$$$$$
class EditorasView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializar

class EditorasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializar

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#%%%%%%%%%%%%%% Livros %%%%%%%%%%%%%%%%%

class LivroView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer 

class LivroDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer 

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    