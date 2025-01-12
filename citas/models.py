from django.db import models

# Create your models here.

from django.contrib.auth.models import User  # Asume que usas el modelo de usuario de Django

class Cita(models.Model):
    ESTADO_CITA = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas')
    fecha_hora = models.DateTimeField()
    motivo = models.TextField(max_length=500, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CITA, default='pendiente')
    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f'Cita con {self.paciente.username} el {self.fecha_hora.strftime("%d/%m/%Y %H:%M")} - {self.estado}'
