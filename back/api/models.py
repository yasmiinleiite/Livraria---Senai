from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    s_nome = models.CharField(max_length=100) 
    nasc = models.DateField(null=True, blank=True)
    nacio = models.CharField(max_length=50, null=True, blank=True)
    biogr = models.TextField()
    
    
    