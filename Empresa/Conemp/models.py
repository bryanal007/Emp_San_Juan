from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=True, unique=True)
    ubicacion = models.CharField(max_length=100, blank=False, null=True)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True)

    def __str__(self):
        return self.nombre

class Puesto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=True)
    salario = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=True)
    apellido = models.CharField(max_length=50, blank=False, null=True)
    cedula = models.CharField(primary_key=True, unique=True, max_length=10, blank=False)
    fecha_nacimiento = models.DateField(blank=False, null=True)
    correo = models.EmailField(unique=True, blank=False)
    celular = models.CharField(max_length=10, blank=True, null=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)

    def __str__(self):
        return self.cedula

class HistorialLaboral(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    empresa_anterior = models.CharField(max_length=100, blank=False, null=True)
    puesto_anterior = models.CharField(max_length=50, blank=False, null=True)
    fecha_inicio = models.DateField(blank=False, null=True)
    fecha_fin = models.DateField(blank=False, null=True)

    def __str__(self):
        return f"{self.empleado.cedula} - {self.empresa_anterior}"

class Evaluacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_evaluacion = models.DateField(blank=False, null=True)
    puntaje = models.DecimalField(max_digits=3, decimal_places=1, blank=False, null=True)
    comentarios = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Evaluación de {self.empleado.cedula}"
