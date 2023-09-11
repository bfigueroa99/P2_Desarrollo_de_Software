import random
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
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
class PreguntaAleatoria(APIView):
    def get(self, request):
        # Obtén una pregunta aleatoria de la base de datos
        preguntas = Pregunta.objects.all()
        pregunta_aleatoria = random.choice(preguntas)

        # Serializa la pregunta y envía la respuesta
        serializer = PreguntaSerializer(pregunta_aleatoria)
        return Response(serializer.data)

class RellenarBaseDeDatos(APIView):
    def post(self, request):
        try:
            datos_json = request.data["preguntas"]
            
            for pregunta_data in datos_json:
                serializer = PreguntaSerializer(data=pregunta_data)
                if serializer.is_valid():
                    serializer.save()
        
            return Response({"message": "Preguntas agregadas con éxito"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
