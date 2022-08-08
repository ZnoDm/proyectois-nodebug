from django import forms 
from django.forms import fields 
from .models import Categoria

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
        'fechaRegistro': forms.TextInput(attrs={'type': 'date'})

    }
