from django.shortcuts import render, redirect
from DjangoApp.models import *
from .forms import *



def base(request):
    if request.method == "POST":
        form = SubscribForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suscripciones')
        
    else:
        form = SubscribForm()
        
    ctx = {"form": form}      
    return render(request, 'DjangoApp/base.html' ,ctx)


def index(request):
    if request.method == "POST":
        form = SubscribForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suscripciones')
        
    else:
        form = SubscribForm()
        
    ctx = {"form": form} 
    return render(request, 'DjangoApp/index.html', ctx)

    if request.method == "POST":
        form = SubscribForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suscripciones')
        
    else:
        form = SubscribForm()
        
    ctx = {"form": form} 
    return render(request, 'DjangoApp/servicios.html', ctx)

def contacto(request):
    if request.method == "POST":
        form = SubscribForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suscripciones')
        
    else:
        form = SubscribForm()
        
    ctx = {"form": form} 
    return render(request, 'DjangoApp/contacto.html', ctx)

def portfolio(request):
    if request.method == "POST":
        form = SubscribForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suscripciones')
        
    else:
        form = SubscribForm()
        
    ctx = {"form": form} 
    return render(request, 'DjangoApp/portfolio.html', ctx)

def blog(request):
    if request.method == "POST":
        form = SubscribForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suscripciones')
        
    else:
        form = SubscribForm()
    
    comentarios = Comentarios.objects.all()
    
    ctx = {"comentarios": comentarios, "form": form,}  
    return render(request, 'DjangoApp/blog.html', ctx)

def servicios(request):
    if request.method == "POST":
        form = ServiciosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suscripciones')
        
    else:
        form = SubscribForm()
    
    
    servicios = Servicios.objects.all()
        
    ctx = {"form": form, "servicios": servicios} 
    return render(request, 'DjangoApp/servicios.html', ctx)

# -----Vistas Auxiliares-----------

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

def agregarServicio(request):   
    
    if request.method == "POST":
        form = ServiciosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios')
        
    else:
        form = ServiciosForm()   
    
    ctx = {"form": form}  
    return render(request, 'DjangoApp/agregarServicio.html' ,ctx) 

def suscripciones(request):
    
    suscripciones = Subscripcion.objects.all()  

    ctx = {"suscripciones": suscripciones}  
    return render(request, 'DjangoApp/suscripciones.html' ,ctx)     