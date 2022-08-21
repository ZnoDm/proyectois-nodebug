
from django.urls import path
from seguridadApp.views.views import listarpermiso

urlpatterns = [
    path('',listarpermiso,name="listarpermiso"),  
]