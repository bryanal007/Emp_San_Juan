from django.contrib import admin
from .models import Empleado, Departamento, Puesto, HistorialLaboral, Evaluacion

# Registra los modelos 
admin.site.register(Empleado)
admin.site.register(Departamento)
admin.site.register(Puesto)
admin.site.register(HistorialLaboral)
admin.site.register(Evaluacion)
