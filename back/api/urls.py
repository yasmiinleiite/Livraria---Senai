from django.urls import path
from.views import AutoresView, listar_autores, EditorasView, LivroView

urlpatterns = [
    path('autores', AutoresView.as_view()),
    path('authors', listar_autores),
    path('editoras', EditorasView.as_view()),
    path('livros', LivroView.as_view()),
]
