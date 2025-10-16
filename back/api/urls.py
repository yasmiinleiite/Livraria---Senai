from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"imagens", ImagemViewSet, basename="imagens")
router.register(r"livros", LivrosViw, basename="livros")

urlpatterns = [
    path('autores/', AutoresView.as_view(), name='autores-list'), 
    path('autor/<int:pk>', AutoresDetailView.as_view(), name='autores-detail'),
    path('authors', listar_autores, name='Listar Autores'),
   
    path('editoras', EditorasView.as_view()),
    path('editora/<int:pk>', EditorasDetailView.as_view()),
   
    # path('livros', LivrosView.as_view()),
    path('livro/<int:pk>', LivrosDetailView.as_view()),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('register/', RegisterView.as_view(), name='register'),
    
] 

urlpatterns += router.urls

