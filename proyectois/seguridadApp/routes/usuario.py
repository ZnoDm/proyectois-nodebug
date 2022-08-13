
from django.urls import path
from seguridadApp.views import listarusuario,eliminarusuario,activarusuario

urlpatterns = [
    path('',listarusuario,name="listarusuario"),  
    path('delete/<int:id>/',eliminarusuario,name="eliminarusuario"), 
    path('active/<int:id>/<int:activo>/',activarusuario,name="activarusuario"), 
]