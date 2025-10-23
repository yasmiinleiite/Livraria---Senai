from django.db import models
from django.contrib.auth.models import AbstractUser
import os, uuid

def path_capa(_, filename):
    ext = os.path.splitext(filename)
    return f"capas/{uuid.uuid4().hex}{ext}"

class Autor(models.Model):
    autor = models.CharField(max_length=100)
    s_autor = models.CharField(max_length=100)
    nasc = models.DateField(null=True, blank=True)
    nacio = models.CharField(max_length=50, null=True, blank=True)
    biogr = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.autor} {self.s_autor}"


class Editora(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

    
class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=255)    
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)      #Ligado à tabela de editoras
    isbn = models.CharField(max_length=255)	                            #Código ISBN (único por edição)
    descricao = models.TextField()	                                    #Resumo ou sinopse do livro
    idioma = models.CharField(max_length=255, default="Português")	    #Ex: Português, Inglês
    ano = models.IntegerField()	                                        #IntegerField	Ano de publicação
    paginas = models.IntegerField()         	                        #IntegerField	Número de páginas
    preco = models.DecimalField(max_digits=10, decimal_places=2) 	    #DecimalField	Preço de venda
    estoque = models.IntegerField()	                                    #IntegerField	Quantidade disponível
    desconto = models.DecimalField(max_digits=10, decimal_places=2)	    #DecimalField (opcional)	Valor percentual de desconto
    disponivel = models.BooleanField(default=True)	                    #BooleanField	Se está ativo no catálogo
    dimensoes =	models.CharField(max_length=255)                        #CharField	Tamanho físico do livro
    peso =	models.DecimalField(max_digits=10, decimal_places=2)        #DecimalField	Peso em gramas, se for físico
    capa = models.ImageField(upload_to=path_capa, blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    

class Imagem(models.Model):
    imagem = models.ImageField(upload_to="capas")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem #{self.pk}"
