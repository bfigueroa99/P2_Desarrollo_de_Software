from django.shortcuts import render
from rest_framework import generics
from .models import Pregunta
from .serializers import PreguntaSerializer

class ListaPreguntas(generics.ListCreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class DetallePregunta(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
# views.py
# views.py
from django.http import JsonResponse
from .models import Pregunta

def get_random_question(request):
    # Obtiene una pregunta al azar de la base de datos
    random_question = Pregunta.objects.order_by('?').first()
    
    # Convierte la pregunta en un diccionario serializable
    data = {
        'id': random_question.id,
        'tema': random_question.tema,
        'tipo': random_question.tipo,
        'nivel_dificultad': random_question.nivel_dificultad,
        'enunciado': random_question.enunciado,
        'respuesta': random_question.respuesta,
        'alternativa2': random_question.alternativa2,
        'alternativa3': random_question.alternativa3,
        'alternativa4': random_question.alternativa4,
        'hint': random_question.hint,
    }

    return JsonResponse(data)
