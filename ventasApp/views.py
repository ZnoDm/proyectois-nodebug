from pydoc import describe
from django.shortcuts import render,redirect 
from VentasApp.models import Categoria 
from django.db.models import Q 
from .forms import CategoriaForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def agregarcategoria(request):
    if request.method=="POST":
        form=CategoriaForm(request.POST)
        if form.is_valid():
            descripcion_categoria = form.cleaned_data.get("descripcion")
            categoria_exits = (Categoria.objects.filter(descripcion=descripcion_categoria).count()>0)
            if categoria_exits:
                messages.info(request, "Categoria ya existe.")
                form=CategoriaForm()
                context={'form':form}
                return render(request,"categoria/agregar.html",context) 
            else:
                form.save() 
                return redirect("listarcategoria") 

    else:
        form=CategoriaForm()
        context={'form':form} 
        return render(request,"categoria/agregar.html",context) 

def listarcategoria(request):
    
    queryset = request.GET.get("buscar")
    categoria = Categoria.objects.all().order_by('-idCategoria').values()
    if queryset:
        categoria=Categoria.objects.filter(Q(descripcion__icontains=queryset)).distinct().order_by('-idCategoria').values() 
    paginator = Paginator(categoria, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'categoria':categoria}
    return render(request,"categoria/listar.html",{'page_obj': page_obj})

def editarcategoria(request,id):
    categoria=Categoria.objects.get(idCategoria=id)
    if request.method=="POST":
        form=CategoriaForm(request.POST,instance=categoria)
        if form.is_valid():
            form.save() 
            return redirect("listarcategoria") 
    else:
        form=CategoriaForm(instance=categoria)
        context={"form":form} 
        return render(request,"categoria/edit.html",context)

def eliminarcategoria(request,id):
    categoria=Categoria.objects.get(idCategoria=id) 
    categoria.activo=False
    categoria.save()
    return redirect("listarcategoria") 