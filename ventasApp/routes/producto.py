
from django.urls import path
from ventasApp.views import prodcuto

urlpatterns = [
    path('',prodcuto.listarprodcuto,name="listarprodcuto"),
    path('create/',prodcuto.agregarprodcuto ,name="agregarprodcuto"),
    path('edit/<int:id>/',prodcuto.editarprodcuto ,name="editarprodcuto"),
    path('delete/<int:id>/',prodcuto.eliminarprodcuto,name="eliminarprodcuto"), 
    path('active/<int:id>/<int:activo>/',prodcuto.activarprodcuto,name="activarprodcuto"), 
]