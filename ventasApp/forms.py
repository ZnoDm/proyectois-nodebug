from django import forms 
from django.forms import fields 
from .models import *
from django.contrib.auth.models import User

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
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
        }
class FormaPagoForm(forms.ModelForm):
    class Meta:
        model=FormaPago
        fields=[
            'idFormaPago',
            'descripcion',
            'nroCuotas',
            'frecuencia',
            'interes',
            'activo',
            'usuarioRegistro',
            'fechaRegistro',
            ]
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
        }
class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=[
            'codigo',
            'categoria',      
            'nombre',
            'descripcion',
            'marca',
            'modelo',
            'stock',
            'precioUnitario',
            ]


class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=[
            'ruc',
            'razonSocial',
            'nombreComercial',
            'direccion',
            'email',
            'telefono',
            'activo',
            'usuarioRegistro',
            'fechaRegistro',
            ]
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
        }


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
            'usuarioRegistro',
            'fechaRegistro',
            ]
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
        }

        
class TipoClienteForm(forms.ModelForm):
    class Meta:
        model=TipoCliente
        fields=[
            'descripcion',
            'activo',
            'usuarioRegistro',
            'fechaRegistro',
            ]
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
        }

class PedidoVentaForm(forms.ModelForm):
    class Meta:
        model=PedidoVenta
        fields = '__all__'
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
        }
class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenCompra
        fields = '__all__'
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
        }
        

