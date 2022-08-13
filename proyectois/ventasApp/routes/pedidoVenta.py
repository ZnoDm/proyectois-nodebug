
from django.urls import path
from ventasApp.views import pedidoVenta

urlpatterns = [
    path('',pedidoVenta.listarpedidoVenta,name="listarpedidoVenta"),
    path('create/',pedidoVenta.agregarpedidoVenta,name="agregarpedidoVenta"),
    path('edit/<int:id>/',pedidoVenta.editarpedidoVenta,name="editarpedidoVenta"),
    path('delete/<int:id>/',pedidoVenta.eliminarpedidoVenta,name="eliminarpedidoVenta"), 
    path('active/<int:id>/<int:activo>/',pedidoVenta.activarpedidoVenta,name="activarpedidoVenta"),
]