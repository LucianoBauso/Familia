from socket import fromshare
from django import forms

class IntegranteFormulario(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()

class AutoFormulario(forms.Form):
    patente = forms.CharField(max_length=7)
    modelo = forms.CharField(max_length=15)
    anio = forms.IntegerField()
    color = forms.CharField(max_length=15)

class CasaFormulario(forms.Form):
    direccion = forms.CharField(max_length=30)
    altura = forms.IntegerField()