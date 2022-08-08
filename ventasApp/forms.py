from django import forms 
from django.forms import fields 
from .models import *


class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=[
            'descripcion',
            'activo',
            'usuarioRegistro',
            'fechaRegistro',
            ]
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
        }
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=[
            'tipoCliente',
            'nombres',
            'apellidos',
            'direccion',
            'email',
            'telefono',
            'tipoDocumentoIdentidad',
            'documentoIdentidad',
            'activo',
            'usuarioRegistro',
            'fechaRegistro',
            ]
class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields=[
            'user',
            'nombres',
            'apellidos',
            'direccion',
            'email',
            'telefono',
            'sexo',
            'activo',
            ]
        
class TipoClienteForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=[
            'descripcion',
            'activo',
            'usuarioRegistro',
            'fechaRegistro',
            ]

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=[
            'descripcion',
            'activo',
            'usuarioRegistro',
            'fechaRegistro',
            ]