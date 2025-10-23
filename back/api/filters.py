import django_filters as df
from django.db.models import Q
from .models import Autor, Livro 

class LivroFilter(df.filterset):
    id = df.NumberFilter(field_name='id' , lookup_expr='exact')
    titulo = df.CharFilter(field_name='titulo', lookup_expr='icontains')

    def filter_autor(self, qs, name, value):
        if not value: 
            return qs
        return qs.filter(Q(autor__nome__icontains=value) | Q(autor__s_autor__icontains=value))
    
    class Meta: 
        model = Livro
        fields = []
    