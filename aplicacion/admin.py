from django.contrib import admin
from .models import Moto, Accesorio, Taller, Cliente

# Register your models here.
admin.site.register(Moto)
admin.site.register(Accesorio)
admin.site.register(Taller)
admin.site.register(Cliente)