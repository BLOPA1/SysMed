from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .models import Paciente, Consulta

# Página principal del sistema
def pagina_principal(request):
    return render(request, 'pagina_principal.html')

# Vista para el inicio de sesión
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('gestionar_consultas')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

# Vista para gestionar consultas
@login_required
def gestionar_consultas(request):
    consultas = Consulta.objects.filter(doctor=request.user)
    return render(request, 'gestionar_consultas.html', {'consultas': consultas})

# Vista para crear una nueva consulta
@login_required
def crear_consulta(request):
    if request.method == 'POST':
        paciente = Paciente.objects.create(
            nombre_completo=request.POST['nombre_completo'],
            telefono=request.POST['telefono'],
            edad=request.POST['edad'],
        )
        Consulta.objects.create(
            paciente=paciente,
            doctor=request.user,
            fecha=request.POST['fecha'],
            descripcion=request.POST['descripcion'],
            diagnostico=request.POST['diagnostico']
        )
        return redirect('gestionar_consultas')
    return render(request, 'crear_consulta.html')

# Vista para administrar pacientes
@login_required
def administrar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'administrar_pacientes.html', {'pacientes': pacientes})

# Vista para la ficha del paciente
@login_required
def ficha_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    consultas = Consulta.objects.filter(paciente=paciente)
    return render(request, 'ficha_paciente.html', {'paciente': paciente, 'consultas': consultas})

# Vista para añadir una nueva consulta a un paciente existente
@login_required
def nueva_consulta_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        Consulta.objects.create(
            paciente=paciente,
            doctor=request.user,
            fecha=request.POST['fecha'],
            descripcion=request.POST['descripcion'],
            diagnostico=request.POST['diagnostico']
        )
        return redirect('ficha_paciente', paciente_id=paciente.id)
    return render(request, 'nueva_consulta_paciente.html', {'paciente': paciente})

# Vista para ver una consulta
@login_required
def ver_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    return render(request, 'ver_consulta.html', {'consulta': consulta})

# Vista para editar una consulta
@login_required
def editar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == 'POST':
        consulta.fecha = request.POST['fecha']
        consulta.descripcion = request.POST['descripcion']
        consulta.diagnostico = request.POST['diagnostico']
        consulta.save()
        return redirect('ficha_paciente', paciente_id=consulta.paciente.id)
    return render(request, 'editar_consulta.html', {'consulta': consulta})
