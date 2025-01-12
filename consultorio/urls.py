from django.contrib import admin
from django.urls import path, include
from usuarios.views import pagina_principal, login, logout

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # Panel de administración
    path('', pagina_principal, name='pagina_principal'),  # Página principal con botón de login
    path('login/', login, name='login'),  # Página de login
    path('logout/', logout, name='logout'),  # Página para cerrar sesión
    path('consultas/', include('usuarios.urls')),  # URLs de la app "usuarios"
    path('citas/', include('citas.urls')),  # URLs de la app "citas"
]
