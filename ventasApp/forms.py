from django import forms 
from django.forms import fields 
from .models import *
from django.contrib.auth.models import User
import datetime
class PerfilForm(forms.Form):

    last_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    email = forms.EmailField()
class UsuarioForm(forms.Form):

    last_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=120,widget=forms.PasswordInput)
    is_superuser = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_active = forms.BooleanField(required=False)
class UsuarioEditForm(forms.Form):
    last_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    is_superuser = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_active = forms.BooleanField(required=False)
class GroupForm(forms.Form):
    name = forms.CharField(max_length=150)
class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=[
            'descripcion',
            'activo',
            ]
        
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
            ]
            
class FormaPagoForm(forms.ModelForm):
    class Meta:
        model=FormaPago
        fields=[
            'descripcion',
            'nroCuotas',
            'frecuencia',
            'interes',
            'activo',
            ]
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
            'urlImagen',
            'nombreImagen'
            ]
        widgets = {
            'urlImagen': forms.HiddenInput(),
            'nombreImagen': forms.HiddenInput(),
            'codigo': forms.TextInput(attrs={'readonly': True})
        }
        

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
        model=TipoCliente
        fields=[
            'descripcion',
            'activo',
            ]

class PedidoVentaForm(forms.ModelForm):
    class Meta:
        model = PedidoVenta
        fields=[
            'trabajador',
            'cliente',
            'formaPago',
            'codigo',
            'tipoDocumento',
            'fechaEmision',
            'fechaEntrega',
            'tipoMoneda',
            'tasaCambio',
            'tasaIgv',
            'estado'
            ]
        widgets = {
            'fechaEmision': forms.TextInput(attrs={'type': 'date'}),
            'fechaEntrega': forms.TextInput(attrs={'type': 'date'}),
            'codigo': forms.TextInput(attrs={'readonly': True}),
            'tasaCambio':forms.NumberInput(attrs={'step': '0.01'}),
            'tasaIgv': forms.NumberInput(attrs={'step': '0.01'})
        }


class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenCompra
        fields = [
            'trabajador',
            'proveedor',
            'formaPago',
            'codigo',
            'tipoDocumento',
            'fechaEmision',
            'fechaEntrega',
            'tipoMoneda',
            'tasaCambio',
            'tasaIgv',
            'estado',
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'readonly': True}),
            'fechaEmision': forms.TextInput(attrs={'type': 'date'}),
            'fechaEntrega': forms.TextInput(attrs={'type': 'date'}),
        }
        
        
class NotaAlmacenForm(forms.ModelForm):
    class Meta:
        model = NotaAlmacen
        fields = [
            'trabajador',
            'pedidoVenta',
            'ordenCompra',
            'codigo',
            'fechaEmision',
            'fechaEntrega',
            'tipoOperacion',
            'serie',
            'numero',
            'estado',
        ]
        widgets = {
            'serie': forms.TextInput(attrs={'readonly': True}),
            'numero': forms.TextInput(attrs={'readonly': True}),
            'codigo': forms.TextInput(attrs={'readonly': True}),
            'fechaEmision': forms.TextInput(attrs={'type': 'date'}),
            'fechaEntrega': forms.TextInput(attrs={'type': 'date'}),
            
        }