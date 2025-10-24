import django_filters as df
from django.db.models import Q
from .models import Autor, Livro, Editora
 
class LivroFilter(df.FilterSet):
    id = df.NumberFilter(field_name='id', lookup_expr='exact')
    titulo = df.CharFilter(field_name='titulo', lookup_expr='icontains')
    subtitulo = df.CharFilter(field_name='subtitulo', lookup_expr='icontains')
    autor = df.CharFilter(field_name='autor', lookup_expr='icontains')
 
    class Meta:
        model = Livro
        fields = []
 
class AutorFilter(df.FilterSet):
    id = df.NumberFilter(field_name='id', lookup_expr='exact')
    autor = df.CharFilter(field_name='autor', lookup_expr='icontains')
    s_autor = df.CharFilter(field_name='s_autor', lookup_expr='icontains')
    nasc = df.CharFilter(field_name='nasc', lookup_expr='iexact')
 
    class Meta:
        model = Autor
        fields = []
 
class EditoraFilter(df.FilterSet):
    id = df.NumberFilter(field_name='id', lookup_expr='exact')
    editora = df.CharFilter(field_name='editora', lookup_expr='icontains')
 
    class Meta:
        model = Editora
        fields = []
 