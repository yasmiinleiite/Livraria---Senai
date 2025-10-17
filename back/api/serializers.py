from rest_framework import serializers
from .models import Autor, Editora, Livro, Imagem

# === ADICIONE: imports para o cadastro ===
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'


class LivroSerializer(serializers.ModelSerializer):
    capa_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Livro
        fields = [
            "id",
            "titulo", 
            "subtitulo", 
            "autor", 
            "editora", 
            "isbn", 
            "descricao", 
            "idioma", 
            "ano", 
            "paginas", 
            "preco", 
            "estoque", 
            "desconto", 
            "disponivel", 
            "dimensoes", 
            "peso", 
            "capa",
            "capa_url" 
        ]
    
    def get_capa_url(self, obj):
        request = self.context.get("request")
        if obj.capa and request:
            return request.build_absolute_uri(obj.capa.url)  
        return None


        
        
        

# === ADICIONE: serializer de registro de usuário ===
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="Usuário já existe.")]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password],
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )


class ImagemSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Imagem
        fields = ['id', 'imagem', 'url', 'criado_em']
        read_only_fields = ['id', 'url', 'criado_em']

    def get_url(self,obj):
        request = self.context.get("request")
        if request:
            return request.build.absolute_uri(obj.imagem.url)
        return obj.imagem.url