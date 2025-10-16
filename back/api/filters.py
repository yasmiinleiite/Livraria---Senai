########### Caso queira um filtro duplo ################################
import django_filters as df
from django.db.models import Q
from .models import Autor

class AutorFilter(df.FilterSet):
    # ?nome=jorge  → procura em nome OU sobrenome (parcial, sem diferenciar maiúsc/minúsc)
    autor = df.CharFilter(method='filter_nome')

    # ?nacionalidade=brasileira → compara case-insensitive (ex.: "Brasileira" == "brasileira")
    nacio = df.CharFilter(field_name='nacio', lookup_expr='iexact')

    def filter_nome(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(Q(autor__icontains=value) | Q(s_autor__icontains=value))

    class Meta:
        model = Autor
        fields = []  # usamos os campos customizados acima
