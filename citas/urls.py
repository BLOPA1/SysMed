from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_citas, name='listar_citas'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('editar/<int:cita_id>/', views.editar_cita, name='editar_cita'),
    path('calendario/', views.calendario, name='calendario'),
    path('api/citas/', views.api_citas, name='api_citas'),  # Ruta del API de citas
    path('calendario_citas/', views.calendario_citas, name='calendario_citas'),
    path('eliminar/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
]
