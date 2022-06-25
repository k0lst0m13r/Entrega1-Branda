from django.shortcuts import render, redirect
from DjangoApp.models import *
from .forms import *



def index(request):
    return render(request, 'DjangoApp/index.html')

def servicios(request):
    return render(request, 'DjangoApp/servicios.html')

def contacto(request):
    return render(request, 'DjangoApp/contacto.html')

def portfolio(request):
    return render(request, 'DjangoApp/portfolio.html')

def blog(request): 
    
    comentarios = Comentarios.objects.all()
    
    ctx = {"comentarios": comentarios}  
    return render(request, 'DjangoApp/blog.html', ctx)


def comentarios(request):    
    
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        
    else:
        form = CommentForm()   
    
    ctx = {"form": form}  
    return render(request, 'DjangoApp/comentarios.html' ,ctx)    
        