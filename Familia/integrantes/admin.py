from django.contrib import admin
from .models import Casa, Integrante, Auto

# Register your models here.
admin.site.register(Integrante)
admin.site.register(Auto)
admin.site.register(Casa)