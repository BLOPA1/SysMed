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
    pagina_principal,
)

urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('consultas/', gestionar_consultas, name='gestionar_consultas'),
    path('nueva/', crear_consulta, name='crear_consulta'),
    path('pacientes/', administrar_pacientes, name='administrar_pacientes'),
    path('pacientes/<int:paciente_id>/', ficha_paciente, name='ficha_paciente'),
    path('pacientes/<int:paciente_id>/nueva_consulta/', nueva_consulta_paciente, name='nueva_consulta_paciente'),
    path('consulta/<int:consulta_id>/', ver_consulta, name='ver_consulta'),
    path('consulta/<int:consulta_id>/editar/', editar_consulta, name='editar_consulta'),
    path('login/', login, name='login'),
]
