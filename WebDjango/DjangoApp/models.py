from django.db import models



class Comentarios(models.Model):    
    nombre = models.CharField(max_length=15)
    comentario = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    
class Subscripcion(models.Model):    
    email = models.EmailField(max_length=40)
    
    
class Servicios(models.Model):    
    servicio = models.CharField(max_length=20) 