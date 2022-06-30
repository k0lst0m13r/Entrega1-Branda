from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from DjangoApp.models import *
from .forms import *




def log_in(request):    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')
    form =  AuthenticationForm()  
    ctx = {"form": form}    
    return render(request, 'DjangoApp/login.html',ctx)            
    
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
            
            return redirect('index')        
        
        return render(request, 'DjangoApp/registro.html', {"form": form})        
    

    else:
        form = UserCreationForm()
    return render(request, 'DjangoApp/registro.html', {"form": form})


def logout(request):
    loguot(request)
    return redirect('index')

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
    
    if request.method == "POST":
        busqueda = request.POST["buscar"]
        if busqueda == "":
            return redirect('resultadoBusqueda')    
        resultados =  Comentarios.objects.filter(nombre__icontains=busqueda)
        ctx = {"resultados": resultados}            
        return render(request, 'DjangoApp/resultadoBusqueda.html', ctx)  
              
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

def resultadoBusqueda(request):        
    return render(request, 'DjangoApp/resultadoBusqueda.html') 
  
def crearPost(request):   
    
    if request.method == "POST":
        form = CrearPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        
    else:
        form = CrearPost()   
    
    ctx = {"form": form}  
    return render(request, 'DjangoApp/crearPost.html' ,ctx)
    