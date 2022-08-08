from django.contrib import admin
from .models import Cliente
# Register your models here.
class ClienteAdmin(admin.ModelAdmin): 
    list_display=("nombres")

admin.site.register(Cliente)