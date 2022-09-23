from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('casas/',views.casas),
    path('autos/',views.autos),
    path('integranteFormulario/', views.integranteFormulario),
    path('autoFormulario/', views.autoFormulario),
    path('casaFormulario/', views.casaFormulario),
    path('busquedaNombreIntegrante/', views.busquedaNombreIntegrante, name="BusquedaNombre"),
    path('buscar/', views.buscar),
]