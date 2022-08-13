from pydoc import describe
from django.shortcuts import render,redirect 
from ventasApp.models import OrdenCompra 
from django.db.models import Q 
from ventasApp.forms import OrdenCompraForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def agregarordenCompra(request):
    if request.method=="POST":
        form=OrdenCompraForm(request.POST)
        if form.is_valid():
            codigo_ordenCompra = form.cleaned_data.get("codigo")
            ordenCompra_exits = (OrdenCompra.objects.filter(codigo=codigo_ordenCompra).count()>0)
            if ordenCompra_exits:
                messages.info(request, "Orden de compra ya existente.")
                form=OrdenCompraForm()
                context={'form':form}
                return render(request,"ordenCompra/agregar.html",context) 
            else:
                messages.success(request, "Orden de compra registrada.")
                form.save() 
                return redirect("listarordenCompra") 
    
    else:
        form=OrdenCompraForm()
        context={'form':form} 
        return render(request,"ordenCompra/agregar.html",context) 

def listarordenCompra(request):
    queryset = request.GET.get("buscar")
    ordenCompra = OrdenCompra.objects.all().filter(eliminado=False).order_by('-idOrdenCompra').values()
    if queryset:
        ordenCompra=OrdenCompra.objects.filter(Q(codigo__icontains=queryset)).filter(eliminado=False).distinct().order_by('-idOrdenCompra').values() 
    paginator = Paginator(ordenCompra, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'ordenCompra':ordenCompra}
    return render(request,"ordenCompra/listar.html",{'page_obj': page_obj})

def editarordenCompra(request,id):
    ordenCompra=OrdenCompra.objects.get(idOrdenCompra=id)
    if request.method=="POST":
        form=OrdenCompraForm(request.POST,instance=ordenCompra)
        if form.is_valid():
            messages.success(request, "Orden actualizada.")
            form.save() 
            return redirect("listarordenCompra") 
    else:
        form=OrdenCompraForm(instance=ordenCompra)
        context={"form":form} 
        return render(request,"ordenCompra/edit.html",context)

def eliminarordenCompra(request,id):
    ordenCompra=OrdenCompra.objects.get(idOrdenCompra=id) 
    ordenCompra.activo=False
    ordenCompra.eliminado=True
    ordenCompra.save()
    messages.success(request, "Orden de compra eliminada.")
    return redirect("listarordenCompra")

def activarordenCompra(request,id,activo):
    ordenCompra=OrdenCompra.objects.get(idOrdenCompra=id)
    if activo == 0:
        ordenCompra.activo=True
    else:
        ordenCompra.activo=False
    ordenCompra.save()
    messages.success(request, "Orden de compra actualizada.")
    return redirect("listarordenCompra") 