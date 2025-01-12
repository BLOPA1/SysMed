from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Cita
from .forms import CitaForm
from django.utils.dateparse import parse_datetime

def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'citas/listar_citas.html', {'citas': citas})

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm()
    return render(request, 'citas/crear_cita.html', {'form': form})

def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'citas/editar_cita.html', {'form': form, 'cita': cita})

def calendario(request):
    """
    Renderiza la página del calendario interactivo.
    """
    return render(request, 'citas/calendario.html')

def calendario_citas(request):
    citas = Cita.objects.all()
    eventos = []
    for cita in citas:
        eventos.append({
            'title': cita.motivo,
            'start': cita.fecha_hora.isoformat(),
            'end': cita.fecha_hora.isoformat(),  # Opcional: puedes incluir duración aquí
        })
    return JsonResponse(eventos, safe=False)

def api_citas(request):
    """
    API para devolver las citas en formato JSON, filtradas por rango de fechas.
    """
    start = request.GET.get('start')  # Fecha inicial enviada por el calendario
    end = request.GET.get('end')  # Fecha final enviada por el calendario

    if start and end:
        # Convertir las fechas de texto a objetos datetime
        start_date = parse_datetime(start)
        end_date = parse_datetime(end)
        # Filtrar citas en el rango de fechas
        citas = Cita.objects.filter(fecha_hora__gte=start_date, fecha_hora__lte=end_date)
    else:
        citas = Cita.objects.all()

    eventos = []
    for cita in citas:
        eventos.append({
            'title': cita.motivo,
            'start': cita.fecha_hora.isoformat(),
            'end': cita.fecha_hora.isoformat(),  # Si tienes duración, cámbialo
        })

    return JsonResponse(eventos, safe=False)

def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == "POST":
        cita.delete()
        return redirect('listar_citas')
    return render(request, 'citas/eliminar_cita.html', {'cita': cita})
