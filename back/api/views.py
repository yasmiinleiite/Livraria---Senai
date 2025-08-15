from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Autor
from .serializers import AutorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status #do rest_framework ele esta importando algo específico

class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

@api_view(['GET', 'POST'])
def listar_autores(request):
    if request.method == 'GET': #get é para pegar do banco 
        queryset = Autor.objects.all() #coloca todos os autores 
        serializer = AutorSerializer(queryset, many=True) #serializer vai colocar todos autores em json e o many= true significa ue se tiver mais de um vai também
        return Response(serializer.data) 
    elif request.method == 'POST': #post é para mandar para o banco
        serializer = AutorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(); 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        