from pydoc import describe
from django.shortcuts import render,redirect 
from ventasApp.models import PedidoVenta 
from django.db.models import Q 
from ventasApp.forms import PedidoVentaForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def agregarpedidoVenta(request):
    if request.method=="POST":
        form=PedidoVentaForm(request.POST)
        if form.is_valid():
            codigo_pedidoVenta = form.cleaned_data.get("codigo")
            pedidoVenta_exits = (PedidoVenta.objects.filter(codigo=codigo_pedidoVenta).count()>0)
            if pedidoVenta_exits:
                messages.info(request, "Pedido de venta ya existente.")
                form=PedidoVentaForm()
                context={'form':form}
                return render(request,"pedidoVenta/agregar.html",context) 
            else:
                messages.success(request, "Pedido de venta registrado.")
                form.save() 
                return redirect("listarpedidoVenta") 
    
    else:
        form=PedidoVentaForm()
        context={'form':form} 
        return render(request,"pedidoVenta/agregar.html",context) 

def listarpedidoVenta(request):
    
    queryset = request.GET.get("buscar")
    pedidoVenta = PedidoVenta.objects.all().filter(eliminado=False).order_by('-idPedidoVenta').values()
    if queryset:
        pedidoVenta=PedidoVenta.objects.filter(Q(codigo__icontains=queryset)).filter(eliminado=False).distinct().order_by('-idPedidoVenta').values() 
    paginator = Paginator(pedidoVenta, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'pedidoVenta':pedidoVenta}
    return render(request,"pedidoVenta/listar.html",{'page_obj': page_obj})

def editarpedidoVenta(request,id):
    pedidoVenta=PedidoVenta.objects.get(idPedidoVenta=id)
    if request.method=="POST":
        form=PedidoVentaForm(request.POST,instance=pedidoVenta)
        if form.is_valid():
            messages.success(request, "Pedido actualizado.")
            form.save() 
            return redirect("listarpedidoVenta") 
    else:
        form=PedidoVentaForm(instance=pedidoVenta)
        context={"form":form} 
        return render(request,"pedidoVenta/edit.html",context)

def eliminarpedidoVenta(request,id):
    pedidoVenta=PedidoVenta.objects.get(idPedidoVenta=id) 
    pedidoVenta.activo=False
    pedidoVenta.eliminado=True
    pedidoVenta.save()
    messages.success(request, "Pedido de venta eliminado.")
    return redirect("listarpedidoVenta")

def activarpedidoVenta(request,id,activo):
    pedidoVenta=PedidoVenta.objects.get(idPedidoVenta=id)
    if activo == 0:
        pedidoVenta.activo=True
    else:
        pedidoVenta.activo=False
    pedidoVenta.save()
    messages.success(request, "Pedido de venta actualizado.")
    return redirect("listarpedidoVenta") 