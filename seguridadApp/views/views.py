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
from ventasApp.forms import PerfilForm
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
                request.session['userName_logged'] = usuario.first_name + ' '+ usuario.last_name
                request.session['user_logged'] = usuario.username
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
    return render(request, "home.html",{'userNameLogged':request.session['userName_logged'],'userLogged':request.session['user_logged']})

def salir(request):    
    del request.session['user_logged']
    del request.session['userName_logged']
    logout(request)
    messages.info(request,"Saliste exitosamente")
    return redirect("login") 

def perfil(request):
    user=User.objects.get(username=request.session['user_logged'])
    request.session['userName_logged'] = user.last_name + ' '+ user.first_name
    if request.method=="POST":
        form=PerfilForm(request.POST)
        if form.is_valid():
            messages.success(request, "Perfil actualizado.")
            user.last_name=form.cleaned_data.get("last_name")
            user.first_name=form.cleaned_data.get("first_name")
            user.email=form.cleaned_data.get("email")
            user.save()
            return redirect("perfil")
    else:
        initial_dict = {
            "last_name":user.last_name,"first_name":user.first_name,"email":user.email
        }
        form=PerfilForm(initial=initial_dict)
        context={"form":form,'userNameLogged':request.session['userName_logged']} 
        return render(request,"datospersonales/edit.html",context)
    


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