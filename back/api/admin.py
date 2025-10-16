from django.contrib import admin
from .models import Autor, Editora, Livro

admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Livro)

# from django.contrib import admin
# from .models import Livro

# class LivroAdmin(admin.ModelAdmin):
#     list_display = ['titulo', 'autor', 'editora', 'isbn', 'ano_publicacao', 'preco', 'estoque', 'disponivel']

# admin.site.register(Livro, LivroAdmin)

