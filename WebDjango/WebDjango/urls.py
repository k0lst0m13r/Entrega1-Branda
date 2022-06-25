"""WebDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DjangoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('servicios',views.servicios, name="servicios"),
    path('contacto',views.contacto, name="contacto"),
    path('portfolio',views.portfolio, name="portfolio"),
    path('blog',views.blog, name="blog"),
    path('comentarios',views.comentarios, name="comentarios"),
    path('suscripciones',views.suscripciones, name="suscripciones"),
    
]
