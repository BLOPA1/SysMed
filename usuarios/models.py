from django.db import models
from django.contrib.auth.models import User

# Modelo para representar un paciente
class Paciente(models.Model):
    nombre_completo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_completo

# Modelo para representar las consultas médicas
class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    descripcion = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)  # Nuevo campo para diagnóstico

    def __str__(self):
        return f"{self.paciente.nombre_completo} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"
