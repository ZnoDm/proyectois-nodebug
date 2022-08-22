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
            ]

        
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
        model = PedidoVenta
        fields = '__all__'
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
            'fechaEmision': forms.TextInput(attrs={'type': 'date'}),
            'fechaModificacion': forms.TextInput(attrs={'type': 'date'}),
            'fechaEliminacion': forms.TextInput(attrs={'type': 'date'}),
            'fechaEntrega': forms.TextInput(attrs={'type': 'date'}),
        }


class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenCompra
        fields = '__all__'
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
            'fechaEmision': forms.TextInput(attrs={'type': 'date'}),
            'fechaModificacion': forms.TextInput(attrs={'type': 'date'}),
            'fechaEliminacion': forms.TextInput(attrs={'type': 'date'}),
            'fechaEntrega': forms.TextInput(attrs={'type': 'date'}),
        }
        
        
class NotaAlmacenForm(forms.ModelForm):
    class Meta:
        model = NotaAlmacen
        fields = '__all__'
        widgets = {
            'fechaRegistro': forms.TextInput(attrs={'type': 'date'}),
            'fechaEmision': forms.TextInput(attrs={'type': 'date'}),
            'fechaModificacion': forms.TextInput(attrs={'type': 'date'}),
            'fechaEliminacion': forms.TextInput(attrs={'type': 'date'}),
            'fechaEntrega': forms.TextInput(attrs={'type': 'date'}),
        }