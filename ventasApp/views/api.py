from django.shortcuts import render,redirect 
from django.http import JsonResponse
from ventasApp.models import * 

def get_countVentas(request,*args,**kwargs):
    cantidad = PedidoVenta.objects.count()
    data={
        'tipo':'ventas',
        'cantidad': cantidad
    }
    return JsonResponse(data)

def get_countCompras(request,*args,**kwargs):
    cantidad = OrdenCompra.objects.count()
    data={
        'tipo':'compras',
        'cantidad':cantidad
    }
    return JsonResponse(data)

def get_dataLine(request,*args,**kwargs):
    data = {
          'labels': ['January','February','March','April','May','June'],
          'datasets': [{
            'label': 'My First dataset',
            'backgroundColor': 'rgb(255, 99, 132)',
            'borderColor': 'rgb(255, 99, 132)',
            'data': [0, 10, 5, 2, 20, 30, 45],
          }]
    };
    return JsonResponse(data)

def get_dataDona(request,*args,**kwargs):
    data = {
            'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            'datasets': [{
                'label': '# of Votes',
                'data': [12, 19, 3, 5, 2, 3],
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
