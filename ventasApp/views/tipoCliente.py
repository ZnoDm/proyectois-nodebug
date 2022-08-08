from pydoc import describe
from django.shortcuts import render,redirect 
from ventasApp.models import Producto 
from django.db.models import Q 
from ventasApp.forms import CategoriaForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def agregarcategoria(request):
    if request.method=="POST":
        form=CategoriaForm(request.POST)
        if form.is_valid():
            descripcion_categoria = form.cleaned_data.get("descripcion")
            categoria_exits = (Producto.objects.filter(descripcion=descripcion_categoria).count()>0)
            if categoria_exits:
                messages.info(request, "Producto ya existe.")
                form=CategoriaForm()
                context={'form':form}
                return render(request,"producto/agregar.html",context) 
            else:
                messages.success(request, "Producto registrada.")
                form.save() 
                return redirect("listarcategoria") 

    else:
        form=CategoriaForm()
        context={'form':form} 
        return render(request,"producto/agregar.html",context) 

def listarcategoria(request):
    
    queryset = request.GET.get("buscar")
    producto = Producto.objects.all().filter(eliminado=False).order_by('-idCategoria').values()
    if queryset:
        producto=Producto.objects.filter(Q(descripcion__icontains=queryset)).filter(eliminado=False).distinct().order_by('-idCategoria').values() 
    paginator = Paginator(producto, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'producto':producto}
    return render(request,"producto/listar.html",{'page_obj': page_obj})

def editarcategoria(request,id):
    producto=Producto.objects.get(idCategoria=id)
    if request.method=="POST":
        form=CategoriaForm(request.POST,instance=producto)
        if form.is_valid():
            form.save() 
            return redirect("listarcategoria") 
    else:
        form=CategoriaForm(instance=producto)
        context={"form":form} 
        return render(request,"producto/edit.html",context)

def eliminarcategoria(request,id):
    producto=Producto.objects.get(idCategoria=id) 
    producto.activo=False
    producto.eliminado=True
    producto.save()
    messages.success(request, "Producto eliminada.")
    return redirect("listarcategoria")

def activarcategoria(request,id,activo):
    producto=Producto.objects.get(idCategoria=id)
    if activo == 0:
        producto.activo=True
    else:
        producto.activo=False
    producto.save()
    messages.success(request, "Producto actualizada.")
    return redirect("listarcategoria") 