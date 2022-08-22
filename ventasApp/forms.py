from django import forms 
from django.forms import fields 
from .models import *
from django.contrib.auth.models import User

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
            'nombreImagen': forms.HiddenInput()
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
            'fechaEmision',
            'fechaEntrega',
            'tipoMoneda',
            'tasaCambio',
            'subtotal',
            'tasaIgv',
            'descuento',
            'total',
            'estado'
            ]
        widgets = {
            'fechaEmision': forms.TextInput(attrs={'type': 'date'}),
            'fechaEntrega': forms.TextInput(attrs={'type': 'date'}),
        }


class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenCompra
        fields = [
            'trabajador',
            'proveedor',
            'cliente',
            'formaPago',
            'codigo',
            'fechaEmision',
            'fechaEntrega',
            'tipoMoneda',
            'tasaCambio',
            'subtotal',
            'tasaIgv',
            'descuento',
            'total',
            'estado',
        ]
        widgets = {
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
            'fechaEmision': forms.TextInput(attrs={'type': 'date'}),
            'fechaEntrega': forms.TextInput(attrs={'type': 'date'}),
        }