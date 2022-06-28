from django import forms

from .models import *

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = ('nombre', 'comentario',)
        
class SubscribForm(forms.ModelForm):
    
    class Meta:
        model = Subscripcion
        fields = ('email',)        
        
class ServiciosForm(forms.ModelForm):
    
    class Meta:
        model = Servicios
        fields = ('servicio',)        
        
        
class CrearPost(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('titulo', 'post', 'autor',)
        
        
class ImageForm(forms.ModelForm):
    
    class Meta:
        model = ImagenPost
        fields = ('imagen', 'descripcion',)