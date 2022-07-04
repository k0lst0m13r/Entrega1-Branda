from django.db import models



class Comentarios(models.Model):    
    nombre = models.CharField(max_length=40)
    comentario = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre, self.creado

    
class Servicios(models.Model):    
    servicio = models.CharField(max_length=30)
    def __str__(self):
        return self.servicio 

    
class Post(models.Model):
    titulo = models.CharField(max_length=40)
    post = models.TextField()
    autor = models.CharField(max_length=40)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo, self. autor, self.fecha
    

class ImagenPost(models.Model):
    descripcion = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to = "images/")
    def __str__(self):
        return self.descripcion

