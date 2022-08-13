from django.contrib import admin
from ventasApp.models import Cliente,Categoria
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombres","activo")
class CategoriaAdmin(admin.ModelAdmin):
    list_display=("descripcion","activo")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)