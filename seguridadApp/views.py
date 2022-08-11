from wsgiref.validate import validator
from django.forms import Form
from django.shortcuts import render, redirect
from typing import Generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User,Permission,Group
from django.core.paginator import Paginator
from django.db.models import Q 
# Create your views here.
def acceder(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)              
                request.session['user_logged'] = usuario.first_name + ' '+ usuario.last_name
                return redirect("home")
            else:
                messages.error(request, "Datos incorrecto.")
        else:
            nombre_usuario=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user_exits=(User.objects.filter(username=nombre_usuario).count()>0)
            if user_exits:
                messages.error(request, "Password incorrecto.")
            else:
                messages.error(request, "Usuario incorrecto.")
    form=AuthenticationForm()
    return render(request, "login.html", {"form": form})

def home(request):
    return render(request, "home.html",{'userLogged':request.session['user_logged']})

def salir(request):    
    del request.session['user_logged']
    logout(request)
    messages.info(request,"Saliste exitosamente")
    return redirect("login") 

def listarusuario(request):    
    queryset = request.GET.get("buscar")
    usuario = User.objects.all().order_by('-id').values()
    if queryset:
        usuario=User.objects.filter(Q(username__icontains=queryset)).distinct().order_by('-id').values()
    paginator = Paginator(usuario, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"usuario/listar.html",{'page_obj': page_obj})
def eliminarusuario(request,id):
    usuario=User.objects.get(id=id) 
    usuario.activo=False
    usuario.eliminado=True
    usuario.save()
    messages.success(request, "User eliminado.")
    return redirect("listarusuario")

def activarusuario(request,id,activo):
    usuario=User.objects.get(id=id)
    if activo == 0:
        usuario.is_staff=True
    else:
        usuario.is_staff=False
    usuario.save()
    messages.success(request, "User actualizado.")
    return redirect("listarusuario") 

def listarpermiso(request):    
    queryset = request.GET.get("buscar")
    permiso = Permission.objects.all().order_by('-id').values()
    if queryset:
        permiso = Permission.objects.filter(Q(name__icontains=queryset)).distinct().order_by('-id').values() 
    paginator = Paginator(permiso, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"permiso/listar.html",{'page_obj': page_obj})

def listarrole(request):    
    queryset = request.GET.get("buscar")
    role = Group.objects.all().order_by('-id').values()
    if queryset:
        role = Group.objects.filter(Q(name__icontains=queryset)).distinct().order_by('-id').values() 
    paginator = Paginator(role,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"role/listar.html",{'page_obj': page_obj})