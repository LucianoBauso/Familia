from django.shortcuts import render, redirect
from .models import Integrante, Casa, Auto
from .forms import IntegranteFormulario, AutoFormulario, CasaFormulario
from django.http import HttpResponse


# Create your views here.
def home (request):
    integrantes = Integrante.objects.all()
    return render(request, 'integrante.html',{'integrante': integrantes})

def casas (request):
    casas = Casa.objects.all()
    return render(request, 'casas.html',{'casa': casas})

def autos (request):
    autos = Auto.objects.all()
    return render(request, 'autos.html',{'auto': autos})

def integranteFormulario(request):
    if request.method == "POST":
        formulario = IntegranteFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            integrante = Integrante( nombre = informacion['nombre'], apellido = informacion['apellido'], edad = informacion['edad'], fecha_nacimiento = informacion['fecha_nacimiento'])
            integrante.save()
            #return render(request, 'integranteFormulario.html')
            return redirect(home)
    else:
        formulario = IntegranteFormulario()
    return render(request, 'integranteFormulario.html', {"formulario": formulario})

def autoFormulario(request):
    if request.method == "POST":
        formulario = AutoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            integrante = Auto( patente = informacion['patente'], modelo = informacion['modelo'], anio = informacion['anio'], color = informacion['color'])
            integrante.save()
            #return render(request, 'autoFormulario.html')
            return redirect(autos)
    else:
        formulario = AutoFormulario()
    return render(request, 'autoFormulario.html', {"formulario": formulario})

def casaFormulario(request):
    if request.method == "POST":
        formulario = CasaFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            integrante = Casa( direccion = informacion['direccion'], altura = informacion['altura'])
            integrante.save()
            #return render(request, 'casaFormulario.html')
            return redirect(casas)
    else:
        formulario = CasaFormulario()
    return render(request, 'casaFormulario.html', {"formulario": formulario})

def busquedaNombreIntegrante(request):
    return render(request,'busquedaNombreIntegrante.html')

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        integrantes = Integrante.objects.filter(nombre__icontains = nombre)

        return render(request, "resultadosBusqueda.html", {"nombre": nombre, "integrantes": integrantes})

    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)