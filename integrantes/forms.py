from socket import fromshare
from django import forms

class IntegranteFormulario(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()