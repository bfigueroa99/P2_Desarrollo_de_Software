import random
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Pregunta, Respuesta
from .serializers import PreguntaSerializer, RespuestaSerializer
from sympy import simplify
# from .features.inner_loop import inner_loop


def get_random_question(request):
    # Obtén todas las preguntas de la base de datos
    preguntas = list(Pregunta.objects.all())
    
    # Baraja aleatoriamente las preguntas para obtener un orden aleatorio
    random.shuffle(preguntas)
    
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

from django.http import JsonResponse
from random import shuffle
from .models import Pregunta

def select_next_question(request):
    # Obtén las preguntas respondidas del cuerpo de la solicitud
    preguntas_respondidas = request.data.get('preguntas_respondidas', [])

    # Obtén el nivel del alumno (puedes pasarlo en el cuerpo de la solicitud)
    nivel_alumno = request.data.get('nivel_alumno', 5)

    # Umbral y variables de racha
    umbral_racha_buenas = 2
    umbral_racha_mala = 2
    racha_buena = 0
    racha_mala = 0

    # Contadores
    cb_tmp = 0
    cm_tmp = 0
    count_hint = 0
    count_alternativas = 0
    count_calculonumerico = 0

    for p in preguntas_respondidas:
        if p['respondida_correctamente']:
            cb_tmp += 1
            cm_tmp = 0
            if cb_tmp >= umbral_racha_buenas:
                racha_buena += 1
        else:
            cm_tmp += 1
            cb_tmp = 0
            if cm_tmp >= umbral_racha_mala:
                racha_mala += 1

        if p['uso_hint']:
            count_hint += 1

        if p['tipo_pregunta'] == 'alternativas':
            count_alternativas += 1

        if p['tipo_pregunta'] == 'calculonumerico':
            count_calculonumerico += 1

    puntaje = ((nivel_alumno * 0.6) + (racha_buena * 0.4) - (count_hint * 0.1) - (racha_mala * 0.3))

    # Calcula el nivel de dificultad
    if puntaje <= 3:
        nivel_dificultad = 'baja'
    elif 3 < puntaje <= 7:
        nivel_dificultad = 'media'
    else:
        nivel_dificultad = 'alta'

    # Lista de preguntas disponibles
    preguntas_disponibles = Pregunta.objects.all()#.exclude(id__in = [p.get('pregunta_relacionada') for p in preguntas_respondidas])

    if not count_alternativas == 5:
        # Filtra preguntas de tipo "alternativas" del mismo tema y nivel de dificultad
        preguntas = preguntas_disponibles.filter(
            tema=preguntas_respondidas[-1]['tema'],
            nivel_dificultad=nivel_dificultad,
            tipo='alternativas'
        )
    elif not count_calculonumerico == 2:
        # Filtra preguntas de tipo "calculonumerico" del mismo tema
        preguntas = preguntas_disponibles.filter(
            tema=preguntas_respondidas[-1]['tema'],
            tipo='calculonumerico'
        )
    else:
        return JsonResponse({"mensaje": "Ya se respondieron todas las preguntas"})

    # Baraja aleatoriamente las preguntas
    preguntas = list(preguntas)
    shuffle(preguntas)

    print(preguntas)

    # Elige la siguiente pregunta (puede ser la primera que coincida)
    if preguntas:
        pregunta = preguntas[0]
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
        return pregunta_data
    else:
        return ("No hay preguntas disponibles")


class SiguientePregunta(APIView):
    def post(self, request):
        # Obtén las preguntas respondidas del cuerpo de la solicitud
        preguntas_respondidas = request.data.get('preguntas_respondidas', [])

        # Obtén el nivel del alumno (puedes pasarlo en el cuerpo de la solicitud)
        nivel_alumno = request.data.get('nivel_alumno', 5)

        # Llama a la función para seleccionar la siguiente pregunta
        siguiente_pregunta = select_next_question(request)

        return Response(siguiente_pregunta)

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

class RegistrarRespuesta(APIView):
    def post(self, request):
        # Obtén los datos de la respuesta del estudiante desde la solicitud
        datos_respuesta = request.data

        # Serializa los datos de la respuesta utilizando el serializador RespuestaSerializer
        serializer = RespuestaSerializer(data=datos_respuesta)

        if serializer.is_valid():
            # Agrega el tipo de pregunta a la respuesta antes de guardarla
            serializer.save(tipo_pregunta=datos_respuesta.get('tipo_pregunta'))

            # Si los datos son válidos, guarda la respuesta en la base de datos
            serializer.save()
            return Response({"mensaje": "Respuesta registrada con éxito"}, status=status.HTTP_201_CREATED)
        else:
            # Si los datos no son válidos, devuelve un mensaje de error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListaRespuestas(generics.ListAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer


class EliminarTodasLasRespuestas(APIView):
    def delete(self, request, *args, **kwargs):
        try:
            # Elimina todas las respuestas de la base de datos
            Respuesta.objects.all().delete()
            return Response({"mensaje": "Todas las respuestas han sido eliminadas"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"mensaje": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


