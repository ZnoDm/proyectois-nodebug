from pydoc import describe
from django.shortcuts import render,redirect 
from ventasApp.models import * 
from django.db.models import Q 
from ventasApp.forms import OrdenCompraForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def agregarordenCompra(request):
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
        return redirect("listarordenCompra") 
    
    else:
        form=OrdenCompraForm(initial={'tasaIgv': 0.18,'tasaCambio': 0})
        context={'form':form,'list_product':list_product} 
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