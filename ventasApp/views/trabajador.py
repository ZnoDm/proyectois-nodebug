from pydoc import describe
from django.shortcuts import render,redirect 
from ventasApp.models import Trabajador 
from django.db.models import Q 
from ventasApp.forms import TrabajadorForm
from django.contrib import messages
from django.core.paginator import Paginator
import datetime
# Create your views here.
def agregartrabajador(request):
    if request.method=="POST":
        form=TrabajadorForm(request.POST)
        if form.is_valid():
            email_trabajador = form.cleaned_data.get("email")
            trabajador_exits = (Trabajador.objects.filter(email=email_trabajador).count()>0)
            if trabajador_exits:
                messages.info(request, "Trabajador ya existe.")
                form=TrabajadorForm(initial={'fechaRegistro': 
                datetime.datetime.now()})
                context={'form':form}
                return render(request,"trabajador/agregar.html",context) 
            else:
                messages.success(request, "Trabajador registrada.")
                form.save() 
                return redirect("listartrabajador") 

    else:
        form=TrabajadorForm(initial={'fechaRegistro': 
                datetime.datetime.now()})
        context={'form':form} 
        return render(request,"trabajador/agregar.html",context) 

def listartrabajador(request):
    
    queryset = request.GET.get("buscar")
    trabajador = Trabajador.objects.all().filter(eliminado=False).order_by('-idTrabajador').values()
    if queryset:
        trabajador=Trabajador.objects.filter(Q(email__icontains=queryset)).distinct().filter(eliminado=False).order_by('-idTrabajador').values() 
    paginator = Paginator(trabajador, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'trabajador':trabajador}
    return render(request,"trabajador/listar.html",{'page_obj': page_obj})

def editartrabajador(request,id):
    trabajador=Trabajador.objects.get(idTrabajador=id)
    if request.method=="POST":
        form=TrabajadorForm(request.POST,instance=trabajador)
        if form.is_valid():
            messages.success(request, "Trabajador actualizado.")
            form.save() 
            return redirect("listartrabajador") 
    else:
        form=TrabajadorForm(instance=trabajador)
        context={"form":form} 
        return render(request,"trabajador/edit.html",context)

def eliminartrabajador(request,id):
    trabajador=Trabajador.objects.get(idTrabajador=id) 
    trabajador.activo=False
    trabajador.eliminado=True
    trabajador.save()
    messages.success(request, "Trabajador eliminado.")
    return redirect("listartrabajador")

def activartrabajador(request,id,activo):
    trabajador=Trabajador.objects.get(idTrabajador=id)
    if activo == 0:
        trabajador.activo=True
    else:
        trabajador.activo=False
    trabajador.save()
    messages.success(request, "Trabajador actualizado.")
    return redirect("listartrabajador") 