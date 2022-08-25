
from django.urls import path
from ventasApp.views.dashboard import *

urlpatterns = [
    path('get_countCompras/',get_countCompras ,name="get_countCompras"),
    path('get_countVentas/',get_countVentas ,name="get_countVentas"),
    path('get_dataDona/',get_dataDona,name="get_dataDona"), 
    path('get_dataLine/',get_dataLine,name="get_dataLine"), 
]
