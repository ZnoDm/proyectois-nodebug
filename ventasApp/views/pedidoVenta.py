from pydoc import describe
from django.shortcuts import render,redirect 
from ventasApp.models import FormaPago 
from django.db.models import Q 
from ventasApp.forms import FormaPagoForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def agregarcategoria(request):
    if request.method=="POST":
        form=FormaPagoForm(request.POST)
        if form.is_valid():
            descripcion_categoria = form.cleaned_data.get("descripcion")
            categoria_exits = (FormaPago.objects.filter(descripcion=descripcion_categoria).count()>0)
            if categoria_exits:
                messages.info(request, "FormaPago ya existe.")
                form=FormaPagoForm()
                context={'form':form}
                return render(request,"formaPago/agregar.html",context) 
            else:
                messages.success(request, "FormaPago registrada.")
                form.save() 
                return redirect("listarcategoria") 

    else:
        form=FormaPagoForm()
        context={'form':form} 
        return render(request,"formaPago/agregar.html",context) 

def listarcategoria(request):
    
    queryset = request.GET.get("buscar")
    formaPago = FormaPago.objects.all().filter(eliminado=False).order_by('-idFormaPago').values()
    if queryset:
        formaPago=FormaPago.objects.filter(Q(descripcion__icontains=queryset)).filter(eliminado=False).distinct().order_by('-idFormaPago').values() 
    paginator = Paginator(formaPago, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'formaPago':formaPago}
    return render(request,"formaPago/listar.html",{'page_obj': page_obj})

def editarcategoria(request,id):
    formaPago=FormaPago.objects.get(idFormaPago=id)
    if request.method=="POST":
        form=FormaPagoForm(request.POST,instance=formaPago)
        if form.is_valid():
            messages.success(request, "Cliente actualizado.")
            form.save() 
            return redirect("listarcategoria") 
    else:
        form=FormaPagoForm(instance=formaPago)
        context={"form":form} 
        return render(request,"formaPago/edit.html",context)

def eliminarcategoria(request,id):
    formaPago=FormaPago.objects.get(idFormaPago=id) 
    formaPago.activo=False
    formaPago.eliminado=True
    formaPago.save()
    messages.success(request, "FormaPago eliminada.")
    return redirect("listarcategoria")

def activarcategoria(request,id,activo):
    formaPago=FormaPago.objects.get(idFormaPago=id)
    if activo == 0:
        formaPago.activo=True
    else:
        formaPago.activo=False
    formaPago.save()
    messages.success(request, "FormaPago actualizada.")
    return redirect("listarcategoria") 