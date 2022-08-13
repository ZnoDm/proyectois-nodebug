
from django.urls import path
from ventasApp.views import ordenCompra

urlpatterns = [
    path('',ordenCompra.listarordenCompra,name="listarordenCompra"),
    path('create/',ordenCompra.agregarordenCompra ,name="agregarordenCompra"),
    path('edit/<int:id>/',ordenCompra.editarordenCompra ,name="editarordenCompra"),
    path('delete/<int:id>/',ordenCompra.eliminarordenCompra,name="eliminarordenCompra"), 
    path('active/<int:id>/<int:activo>/',ordenCompra.activarordenCompra,name="activarordenCompra"),
]