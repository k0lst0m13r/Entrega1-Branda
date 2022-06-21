from django.shortcuts import render

def index(request):
    return render(request, 'DjangoApp/index.html')

def servicios(request):
    return render(request, 'DjangoApp/servicios.html')

def contacto(request):
    return render(request, 'DjangoApp/contacto.html')

def portfolio(request):
    return render(request, 'DjangoApp/portfolio.html')

def blog(request):
    return render(request, 'DjangoApp/blog.html')