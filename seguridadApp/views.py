from wsgiref.validate import validator
from django.forms import Form
from django.shortcuts import render, redirect
from typing import Generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


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
                request.session['user_logged'] = nombre_usuario
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
    context={}
    return render(request, "home.html",{'userLogged':request.session['user_logged']})

def salir(request):    
    del request.session['user_logged']
    logout(request)
    messages.info(request,"Saliste exitosamente")
    return redirect("login") 