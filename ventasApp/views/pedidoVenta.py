from django.http import HttpResponse
from pydoc import describe
from django.shortcuts import render,redirect 
from ventasApp.models import *
from django.db.models import Q 
from ventasApp.forms import PedidoVentaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView, View

from ventasApp.utils import render_to_pdf

# Create your views here.
def agregarpedidoVenta(request):
    list_product = Producto.objects.all().filter(eliminado=False).values()
    if request.method=="POST":
        form=PedidoVentaForm(request.POST)

        arregloObjetoProductos = []  
        pedidoVenta_subtotal = 0.0
        pedidoVenta_descuento = 0.0
        pedidoVenta_total = 0.0

        idProducto = request.POST.getlist('idProducto[]')
        idCantidad = request.POST.getlist('idCantidad[]')
        idPrecioUnitario = request.POST.getlist('idPrecioUnitario[]')
        idDescuentoUnitario = request.POST.getlist('idDescuentoUnitario[]')
        idPrecioProductoTotal = request.POST.getlist('idPrecioProductoTotal[]')
        i=0
        while i<len(idProducto):
            pedidoVenta_subtotal = pedidoVenta_subtotal+(float(idCantidad[i])*float(idPrecioUnitario[i]))
            pedidoVenta_descuento = pedidoVenta_descuento+float(idDescuentoUnitario[i])
            pedidoVenta_total = pedidoVenta_total+float(idPrecioProductoTotal[i])

            arregloObjetoProductos.append({
                'Producto':idProducto[i],
                'Cantidad':idCantidad[i],
                'PrecioUnitario':idPrecioUnitario[i],
                'DescuentoUnitario':idDescuentoUnitario[i],
                'PrecioProductoTotal':idPrecioProductoTotal[i],
            })
            i+=1
        
        pedidoVenta = PedidoVenta.objects.create(
                        trabajador = Trabajador.objects.get(idTrabajador=form['trabajador'].value()),
                        cliente = Cliente.objects.get(idCliente=form['cliente'].value()),
                        formaPago = FormaPago.objects.get(idFormaPago=form['formaPago'].value()),
                        codigo = form['codigo'].value(),
                        fechaEmision = form['fechaEmision'].value(),
                        fechaEntrega = form['fechaEntrega'].value(),
                        tipoMoneda = form['tipoMoneda'].value(),
                        tasaCambio = form['tasaCambio'].value(),
                        
                        tasaIgv = form['tasaIgv'].value(),
                        estado = form['estado'].value(),

                        subtotal = pedidoVenta_subtotal,
                        descuento = pedidoVenta_descuento,
                        total = pedidoVenta_total,

                        usuarioRegistro = request.session['user_logged']
                    )
        pedidoVenta.save()
        element = PedidoVenta.objects.all().last()

        for p in arregloObjetoProductos:
            detalle = DetallePedidoVenta(
                pedidoVenta = element,
                producto= Producto.objects.get(idProducto=p['Producto']), 
                cantidad=p['Cantidad'],
                precioUnitario=p['PrecioUnitario'],
                descuentoUnitario=p['DescuentoUnitario'],
                precio=p['PrecioProductoTotal'],
                usuarioRegistro = request.session['user_logged']
            )
            detalle.save()
        messages.success(request, "Pedido de Venta registrada.")
        return redirect("listarpedidoVenta") 
    
    else:
        cantidad = PedidoVenta.objects.count()
        form=PedidoVentaForm(initial={'tasaIgv': 0.18,'tasaCambio': 0,'codigo': str('PV-') + str(cantidad+1)})
        context={'form':form,'list_product':list_product} 
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
    pedidoVenta.usuarioEliminacion = request.session['user_logged']
    pedidoVenta.fechaEliminacion = datetime.datetime.now()
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
    
def ListPedidoVentaPdf(View, id):
        pedidoVenta = PedidoVenta.objects.get(idPedidoVenta=id)
        data = {
            'pedidoVenta': pedidoVenta
        }
        pdf = render_to_pdf('pedidoVenta/listview.html', data)
        return HttpResponse(pdf, content_type='application/pdf')