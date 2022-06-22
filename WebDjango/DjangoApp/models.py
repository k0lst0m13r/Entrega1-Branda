from django.db import models

class Comentarios(models.Model):
    
    nombre = models.CharField(max_length=15)
    coment = models.TextField()