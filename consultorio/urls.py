from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import pagina_principal, login, logout

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # Panel de administración
    path('', pagina_principal, name='pagina_principal'),  # Página principal con botón de login
    path('login/', login, name='login'),  # Página de login
    path('logout/', logout, name='logout'),  # Página para cerrar sesión
    path('consultas/', include('usuarios.urls')),  # URLs de la app "usuarios"
    path('citas/', include('citas.urls')),  # URLs de la app "citas"
]

# Sirviendo archivos estáticos en entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
