from django.shortcuts import render, redirect
from .forms import PreguntaForm
from .models import Pregunta

def crear_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST, request.FILES)
        if form.is_valid():
            pregunta = form.save()
            return redirect('detalle_pregunta', pregunta_id=pregunta.id)
    else:
        form = PreguntaForm()
    
    return render(request, 'tutor_its/crear_pregunta.html', {'form': form})

def ver_pregunta(request, pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    return render(request, 'ver_pregunta.html', {'pregunta': pregunta})



# from .models import PreguntaAlternativa, EjercicioCalculoNumerico

# def inicio(request):
#     # Lógica para la vista de inicio
#     return render(request, 'inicio.html')

# def preguntas_alternativas(request, pregunta_id):
#     # Lógica para la vista de preguntas de alternativas
#     pregunta = PreguntaAlternativa.objects.get(pk=pregunta_id)
#     if request.method == 'POST':
#         # Procesar la respuesta del estudiante y proporcionar retroalimentación
#         # Actualizar el modelo del estudiante aquí según sea necesario
#         return render(request, 'respuesta.html', {'respuesta_correcta': True})  # Ejemplo de respuesta correcta
#     return render(request, 'pregunta_alternativa.html', {'pregunta': pregunta})

# def ejercicios_calculo_numerico(request, ejercicio_id):
#     # Lógica para la vista de ejercicios de cálculo numérico
#     ejercicio = EjercicioCalculoNumerico.objects.get(pk=ejercicio_id)
#     if request.method == 'POST':
#         # Procesar la respuesta del estudiante y proporcionar retroalimentación
#         # Actualizar el modelo del estudiante aquí según sea necesario
#         return render(request, 'respuesta.html', {'respuesta_correcta': True})  # Ejemplo de respuesta correcta
#     return render(request, 'ejercicio_calculo_numerico.html', {'ejercicio': ejercicio})

# def progreso_estudiante(request):
#     # Lógica para la vista de progreso del estudiante
#     # Recopilar información sobre el progreso del estudiante y mostrarla en la plantilla
#     return render(request, 'progreso_estudiante.html')
