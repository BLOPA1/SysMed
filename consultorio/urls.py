from django.contrib import admin
from django.urls import path, include
from usuarios.views import pagina_principal, login  # Importamos la vista de inicio de sesión

urlpatterns = [
    path('admin/', admin.site.urls),  # URL del panel de administración
    path('', pagina_principal, name='pagina_principal'),  # Página principal
    path('login/', login, name='login'),  # URL para inicio de sesión
    path('consultas/', include('usuarios.urls')),  # Incluye las rutas de la app usuarios
]
