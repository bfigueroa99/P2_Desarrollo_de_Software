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

    def perform_create(self, serializer):
        imagen_svg = self.request.data.get('imagen_svg', None)
        if imagen_svg:
            serializer.save(imagen_svg=imagen_svg)
        else:
            serializer.save()

    def perform_update(self, serializer):
        imagen_svg = self.request.data.get('imagen_svg', None)
        if imagen_svg:
            serializer.save(imagen_svg=imagen_svg)
        else:
            serializer.save()

def get_random_question(request):
    # Obtén todas las preguntas de la base de datos
    preguntas = list(Pregunta.objects.all())
    
    # Baraja aleatoriamente las preguntas para obtener un orden aleatorio
    shuffle(preguntas)
    
    # Convierte las preguntas en una lista de diccionarios serializables
    data = []
    for pregunta in preguntas:
        pregunta_data = {
            'id': pregunta.id,
            'tema': pregunta.tema,
            'tipo': pregunta.tipo,
            'nivel_dificultad': pregunta.nivel_dificultad,
            'enunciado': pregunta.enunciado,
            'respuesta': pregunta.respuesta,
            'alternativa1': pregunta.alternativa1,
            'alternativa2': pregunta.alternativa2,
            'alternativa3': pregunta.alternativa3,
            'alternativa4': pregunta.alternativa4,
            'hint': pregunta.hint,
        }
        data.append(pregunta_data)
    
    return JsonResponse(data, safe=False)

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
