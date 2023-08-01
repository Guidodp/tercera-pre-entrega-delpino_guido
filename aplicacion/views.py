from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .migrations import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")



def Cliente(request):
    return render(request, "aplicacion/clientes.html")

def Taller(request):
    return render(request, "aplicacion/talleres.html")

def Moto(request):
    ctx = {"motos": Moto.objects.all() }
    return render(request, "aplicacion/cursos.html", ctx)

def MotoForm(request):
    if request.method == "POST":                
        moto = Moto(nombre=request.POST['nombre'], comision=request.POST['modelo'])
        moto.save()
        return HttpResponse("Se grabo con exito la moto!")
    
    return render(request, "aplicacion/motoForm.html")

def MotoForm2(request):
    if request.method == "POST":   
        miForm = MotoForm(request.POST)
        if miForm.is_valid():
            moto_nombre = miForm.cleaned_data.get('nombre')
            moto_modelo = miForm.cleaned_data.get('modelo')
            moto = Moto(nombre=moto_nombre, comision=moto_modelo)
            moto.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = MotoForm()

    return render(request, "aplicacion/motoForm2.html", {"form":miForm})

def buscarComision(request):
    return render(request, "aplicacion/buscarModelo.html")

def buscar2(request):
    if request.GET['modelo']:
        modelo = request.GET['modelo']
        motos = Moto.objects.filter(modelo__icontains=modelo)
        return render(request, 
                      "aplicacion/resultadosModelo.html", 
                      {"modelo": modelo, "motos":motos})
    return HttpResponse("No se ingresaron datos para buscar!")


#__________________________________
def accesorios(request):
    ctx = {'accesorio': Accesorio.objects.all() }
    return render(request, "aplicacion/accesorios.html", ctx)

def updateAccesorios(request, id_accesorio):
    accesorio = Accesorio.objects.get(id=id_accesorio)
    if request.method == "POST":
        miForm = updateAccesorios(request.POST)
        if miForm.is_valid():
            accesorio.nombre = miForm.cleaned_data.get('nombre')
            accesorio.modelo = miForm.cleaned_data.get('modelo')
            accesorio.marca = miForm.cleaned_data.get('marca')
            accesorio.nacionalidad = miForm.cleaned_data.get('nacionalidad')
            accesorio.save()
            return redirect(reverse_lazy('accesorios'))   
    else:
        miForm = updateAccesorios(initial={'nombre':accesorio.nombre, 
                                       'modelo':accesorio.modelo, 
                                       'marca':accesorio.marca, 
                                       'nacionalidad':accesorio.nacionalidad})         
    return render(request, "aplicacion/profesorForm.html", {'form': miForm})   

def deleteAccesorio(request, id_accesorio):
    accesorio = Accesorio.objects.get(id=id_accesorio)
    accesorio.delete()
    return redirect(reverse_lazy('accesorios'))

def createAccesorio(request):    
    if request.method == "POST":
        miForm = updateAccesorios(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_modelo = miForm.cleaned_data.get('modelo')
            p_marca = miForm.cleaned_data.get('marca')
            p_nacionalidad = miForm.cleaned_data.get('nacionalidad')
            accesorio = Accesorio(nombre=p_nombre, 
                             modelo=p_modelo,
                             marca=p_marca,
                             nacionalidad=p_nacionalidad,
                             )
            accesorio.save()
            return redirect(reverse_lazy('accesorios'))
    else:
        miForm = updateAccesorios()

    return render(request, "aplicacion/accesorioForm.html", {"form":miForm})

#______ Class Based View

class ClienteList(ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')

class ClienteDetail(DetailView):
    model = Cliente

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')    

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')    
