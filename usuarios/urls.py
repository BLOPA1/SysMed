from django.urls import path
from .views import (
    gestionar_consultas,
    crear_consulta,
    administrar_pacientes,
    ficha_paciente,
    nueva_consulta_paciente,
    ver_consulta,
    editar_consulta,
    login,
    inicio,
    pagina_principal,
)

urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),  # Página inicial con botón de login
    path('inicio/', inicio, name='inicio'),  # Página de inicio después del login
    path('consultas/', gestionar_consultas, name='gestionar_consultas'),  # Gestión de consultas
    path('nueva/', crear_consulta, name='crear_consulta'),  # Crear consulta nueva
    path('pacientes/', administrar_pacientes, name='administrar_pacientes'),  # Administrar pacientes
    path('pacientes/<int:paciente_id>/', ficha_paciente, name='ficha_paciente'),  # Ficha del paciente
    path('pacientes/<int:paciente_id>/nueva_consulta/', nueva_consulta_paciente, name='nueva_consulta_paciente'),  # Nueva consulta para paciente
    path('consulta/<int:consulta_id>/', ver_consulta, name='ver_consulta'),  # Ver consulta específica
    path('consulta/<int:consulta_id>/editar/', editar_consulta, name='editar_consulta'),  # Editar consulta específica
    path('login/', login, name='login'),  # Página de login
]
