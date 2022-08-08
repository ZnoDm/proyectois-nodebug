"""proyectois URL Configuration

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
from django.urls import path,include

from seguridadApp.views import acceder,home,salir
from django.contrib.auth import views

from ventasApp.views import listarcategoria,agregarcategoria,editarcategoria,eliminarcategoria

urlpatterns = [
    path('', acceder, name='login'),
    path('home/', home, name='home'),
    path('logout/',salir,name="logout"), 
    
    path('admin/', admin.site.urls),

    path('listacategoria/',listarcategoria,name="listarcategoria"),
    path('agregarcategoria/',agregarcategoria ,name="agregarcategoria"),
    path('editarcategoria/<int:id>/',editarcategoria ,name="editarcategoria"),
    path('eliminarcategoria/<int:id>/',eliminarcategoria,name="eliminarcategoria"), 
]
