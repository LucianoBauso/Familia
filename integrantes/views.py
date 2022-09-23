from asyncio.windows_events import NULL
import http
from http.client import HTTPResponse
from django.shortcuts import render
from .models import Integrante, Casa, Auto
from .forms import IntegranteFormulario
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
            return render(request, 'integranteFormulario.html')
    else:
        formulario = IntegranteFormulario()
    return render(request, 'integranteFormulario.html', {"formulario": formulario})

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