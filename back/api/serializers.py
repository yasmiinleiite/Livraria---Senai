from rest_framework import serializers
from .models import Autor, Editora, Livro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class EditoraSerializar(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Livro 
        fields = '__all__'
        
        

        