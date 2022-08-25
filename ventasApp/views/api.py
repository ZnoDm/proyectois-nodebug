from django.shortcuts import render,redirect 
from django.http import JsonResponse
from ventasApp.models import * 

def get_countVentas(request,*args,**kwargs):
    cantidad = PedidoVenta.objects.filter(eliminado=False).count()
    data={
        'tipo':'ventas',
        'cantidad': cantidad
    }
    return JsonResponse(data)

def get_countCompras(request,*args,**kwargs):
    cantidad = OrdenCompra.objects.filter(eliminado=False).count()
    data={
        'tipo':'compras',
        'cantidad':cantidad
    }
    return JsonResponse(data)

def get_dataLine(request,*args,**kwargs):
    list_trabajadores = []
    list_ventasxtrabajador = []
    trabajadores = Trabajador.objects.all().filter(eliminado=False).order_by('-idTrabajador').values()
    for t in trabajadores:
        trabajador = Trabajador.objects.get(idTrabajador=t['idTrabajador'])
        cuenta = PedidoVenta.objects.filter(trabajador=trabajador).filter(eliminado=False).count()
        list_trabajadores.append(str(t['apellidos'])+str(' ')+str(t['nombres']))
        list_ventasxtrabajador.append(cuenta)
    data = {
          'labels': list_trabajadores,
          'datasets': [{
            'label': 'Cantidad de Ventas',
            'backgroundColor': 'rgb(255, 99, 132)',
            'borderColor': 'rgb(255, 99, 132)',
            'data': list_ventasxtrabajador,
          }]
    };
    return JsonResponse(data)

def get_dataDona(request,*args,**kwargs):
    list_productos = []
    list_cantidadvendidos = []
    productos = Producto.objects.all().filter(eliminado=False).order_by('-idProducto').values()
    for t in productos:
        producto = Producto.objects.get(idProducto=t['idProducto'])
        cuenta = DetallePedidoVenta.objects.filter(producto=producto).filter(eliminado=False).count()
        list_productos.append(str(t['nombre']))
        list_cantidadvendidos.append(cuenta)
    data = {
            'labels': list_productos,
            'datasets': [{
                'label': '# of Votes',
                'data': list_cantidadvendidos,
                'backgroundColor': [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                'borderColor': [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                'borderWidth': 1
            }]
        };
    return JsonResponse(data)
