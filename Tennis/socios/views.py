from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import Socios
from .forms import SociosForm


# Create your views here

def listasocios(request):
    socio=Socios.objects.all()
    return render(request,"CrudSocio/listado.html",{'socio':socio})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarSocio(request,idSocio=0):
      if request.method=="GET":
        if idSocio==0:
            formulario=SociosForm()   
        else:
            sociosid=Socios.objects.get(pk=idSocio)
            formulario=SociosForm(instance=sociosid)
        return render(request,'CrudSocio/Crear.html',{'formulario':formulario})
      else:
        if idSocio==0:
            formulario=SociosForm(request.POST or None, request.FILES or None)
        else:
            sociosid=Socios.objects.get(pk=idSocio)
            formulario=SociosForm(request.POST or None, request.FILES or None ,instance=sociosid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listasocios')
        
def eliminar(request, idSocio):
    bc=Socios.objects.get(id=idSocio)
    bc.delete()
    return redirect('listasocios')
        