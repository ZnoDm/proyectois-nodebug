
from django.urls import path
from seguridadApp.views import listarrole

urlpatterns = [
    path('',listarrole,name="listarrole"),  
]