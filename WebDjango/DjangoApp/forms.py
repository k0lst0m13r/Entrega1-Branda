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