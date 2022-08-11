
from django.urls import path
from seguridadApp.views import listarpermiso

urlpatterns = [
    path('',listarpermiso,name="listarpermiso"),  
]