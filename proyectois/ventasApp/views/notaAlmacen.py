from pydoc import describe
from django.shortcuts import render,redirect 
from ventasApp.models import NotaAlmacen 
from django.db.models import Q 
from ventasApp.forms import NotaAlmacenForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def agregarnotaAlmacen(request):
    if request.method=="POST":
        form=NotaAlmacenForm(request.POST)
        if form.is_valid():
            codigo_notaAlmacen = form.cleaned_data.get("codigo")
            notaAlmacen_exits = (NotaAlmacen.objects.filter(codigo=codigo_notaAlmacen).count()>0)
            if notaAlmacen_exits:
                messages.info(request, "Nota de Almacén ya existente.")
                form=NotaAlmacenForm()
                context={'form':form}
                return render(request,"notaAlmacen/agregar.html",context) 
            else:
                messages.success(request, "Nota de Almacén registrada.")
                form.save() 
                return redirect("listarnotaAlmacen") 
    
    else:
        form=NotaAlmacenForm()
        context={'form':form} 
        return render(request,"notaAlmacen/agregar.html",context) 

def listarnotaAlmacen(request):
    queryset = request.GET.get("buscar")
    notaAlmacen = NotaAlmacen.objects.all().filter(eliminado=False).order_by('-idNotaAlmacen').values()
    if queryset:
        notaAlmacen=NotaAlmacen.objects.filter(Q(codigo__icontains=queryset)).filter(eliminado=False).distinct().order_by('-idNotaAlmacen').values() 
    paginator = Paginator(notaAlmacen, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'notaAlmacen':notaAlmacen}
    return render(request,"notaAlmacen/listar.html",{'page_obj': page_obj})

def editarnotaAlmacen(request,id):
    notaAlmacen=NotaAlmacen.objects.get(idNotaAlmacen=id)
    if request.method=="POST":
        form=NotaAlmacenForm(request.POST,instance=notaAlmacen)
        if form.is_valid():
            messages.success(request, "Orden actualizada.")
            form.save() 
            return redirect("listarnotaAlmacen") 
    else:
        form=NotaAlmacenForm(instance=notaAlmacen)
        context={"form":form} 
        return render(request,"notaAlmacen/edit.html",context)

def eliminarnotaAlmacen(request,id):
    notaAlmacen=NotaAlmacen.objects.get(idNotaAlmacen=id) 
    notaAlmacen.activo=False
    notaAlmacen.eliminado=True
    notaAlmacen.save()
    messages.success(request, "Nota de Almacén eliminada.")
    return redirect("listarnotaAlmacen")

def activarnotaAlmacen(request,id,activo):
    notaAlmacen=NotaAlmacen.objects.get(idNotaAlmacen=id)
    if activo == 0:
        notaAlmacen.activo=True
    else:
        notaAlmacen.activo=False
    notaAlmacen.save()
    messages.success(request, "Nota de Almacén actualizada.")
    return redirect("listarnotaAlmacen") 