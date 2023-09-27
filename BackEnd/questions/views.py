import random
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Pregunta, Respuesta
from .serializers import PreguntaSerializer, RespuestaSerializer
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from random import shuffle

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('dashboard')  # Cambia 'dashboard' a la página a la que deseas redirigir después del registro
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


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



def select_next_question(request):
    # Obtén las preguntas respondidas del cuerpo de la solicitud
    preguntas_respondidas = request.data.get('preguntas_respondidas', [])

    # Obtén el nivel del alumno (puedes pasarlo en el cuerpo de la solicitud)
    nivel_alumno = request.data.get('nivel_alumno', None)

    if nivel_alumno is None:
        return Response({"mensaje": "Nivel del estudiante es campo requerido"}, status=status.HTTP_400_BAD_REQUEST)
    

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
    if puntaje <= 1:
        nivel_dificultad = 'baja'
        tema = 'Diagramas de PVT'
    elif 1 < puntaje <= 2:
        nivel_dificultad = 'media'
        tema = 'Diagramas de PVT'
    elif 2 < puntaje <= 3:
        nivel_dificultad = 'alta'
        tema = 'Diagramas de PVT'
    elif 3 < puntaje <= 4:
        nivel_dificultad = 'baja'
        tema = 'Calidad de mezclas'
    elif 4 < puntaje <= 5:
        nivel_dificultad = 'media'
        tema = 'Calidad de mezclas'
    elif 5 < puntaje <= 6:
        nivel_dificultad = 'alta'
        tema = 'Calidad de mezclas'
    elif 6 < puntaje <= 7:
        nivel_dificultad = 'baja'
        tema = 'Entalpía'
    elif 7 < puntaje <= 8:
        nivel_dificultad = 'media'
        tema = 'Entalpía'
    elif 8 < puntaje <= 9:
        nivel_dificultad = 'alta'
        tema = 'Entalpía'
    elif 9 < puntaje <= 10:
        nivel_dificultad = 'baja'
        tema = 'Calor latente'
    elif 10 < puntaje <= 11:
        nivel_dificultad = 'media'
        tema = 'Calor latente'
    elif 11 < puntaje <= 12:
        nivel_dificultad = 'alta'
        tema = 'Calor latente'
    elif 12 < puntaje <= 13:
        nivel_dificultad = 'baja'
        tema = 'Tabla de saturación'
    elif 13 < puntaje <= 14:
        nivel_dificultad = 'media'
        tema = 'Tabla de saturación'
    elif 14 < puntaje <= 15:
        nivel_dificultad = 'alta'
        tema = 'Tabla de saturación'

    # Lista de preguntas disponibles
    preguntas_disponibles = Pregunta.objects.all().exclude(id__in = [p.get('pregunta_relacionada') for p in preguntas_respondidas])

    if count_alternativas != 3:
        # Filtra preguntas de tipo "alternativas" del mismo tema y nivel de dificultad
        preguntas = preguntas_disponibles.filter(
            tema=tema,
            nivel_dificultad=nivel_dificultad,
            tipo='alternativas'
        )
    if count_calculonumerico != 2:
        # Filtra preguntas de tipo "calculonumerico" del mismo tema
        preguntas = preguntas_disponibles.filter(
            tema=tema,
            tipo='calculonumerico'
        )
    else:
        return nivel_dificultad

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
        return (pregunta_data,puntaje)
    else:
        return ("No hay preguntas disponibles")

class SeleccionarPrimeraPregunta(APIView):
    def post(self, request):
        # Obtén el nivel del estudiante y el tema del cuerpo de la solicitud
        nivel_estudiante = request.data.get('nivel_estudiante', None)

        if nivel_estudiante is None:
            return Response({"mensaje": "Nivel del estudiante es campo requerido"}, status=status.HTTP_400_BAD_REQUEST)

        
        # Calcula el nivel de dificultad
        if nivel_estudiante <= 1:
            nivel_dificultad = 'baja'
            tema = 'Diagramas de PVT'
        elif 1 < nivel_estudiante <= 2:
            nivel_dificultad = 'media'
            tema = 'Diagramas de PVT'
        elif 2 < nivel_estudiante <= 3:
            nivel_dificultad = 'alta'
            tema = 'Diagramas de PVT'
        elif 3 < nivel_estudiante <= 4:
            nivel_dificultad = 'baja'
            tema = 'Calidad de mezclas'
        elif 4 < nivel_estudiante <= 5:
            nivel_dificultad = 'media'
            tema = 'Calidad de mezclas'
        elif 5 < nivel_estudiante <= 6:
            nivel_dificultad = 'alta'
            tema = 'Calidad de mezclas'
        elif 6 < nivel_estudiante <= 7:
            nivel_dificultad = 'baja'
            tema = 'Entalpía'
        elif 7 < nivel_estudiante <= 8:
            nivel_dificultad = 'media'
            tema = 'Entalpía'
        elif 8 < nivel_estudiante <= 9:
            nivel_dificultad = 'alta'
            tema = 'Entalpía'
        elif 9 < nivel_estudiante <= 10:
            nivel_dificultad = 'baja'
            tema = 'Calor latente'
        elif 10 < nivel_estudiante <= 11:
            nivel_dificultad = 'media'
            tema = 'Calor latente'
        elif 11 < nivel_estudiante <= 12:
            nivel_dificultad = 'alta'
            tema = 'Calor latente'
        elif 12 < nivel_estudiante <= 13:
            nivel_dificultad = 'baja'
            tema = 'Tabla de saturación'
        elif 13 < nivel_estudiante <= 14:
            nivel_dificultad = 'media'
            tema = 'Tabla de saturación'
        elif 14 < nivel_estudiante <= 15:
            nivel_dificultad = 'alta'
            tema = 'Tabla de saturación'


        # Filtra las preguntas disponibles basadas en el nivel del estudiante y el tema
        preguntas_disponibles = Pregunta.objects.filter(
            nivel_dificultad__lte=nivel_dificultad,
            tema=tema
        )

        print(preguntas_disponibles)

        if not preguntas_disponibles.exists():
            return Response({"mensaje": "No hay preguntas disponibles para este nivel y tema"}, status=status.HTTP_404_NOT_FOUND)

        # Baraja aleatoriamente las preguntas
        preguntas = list(preguntas_disponibles)
        random.shuffle(preguntas)

        # Obtén la primera pregunta
        primera_pregunta = preguntas[0]

        # Serializa la pregunta y envía la respuesta
        serializer = PreguntaSerializer(primera_pregunta)
        return Response(serializer.data)
    
class SiguientePregunta(APIView):
    def post(self, request):
        # Obtén las preguntas respondidas del cuerpo de la solicitud
        preguntas_respondidas = request.data.get('preguntas_respondidas', [])

        # Obtén el nivel del alumno (puedes pasarlo en el cuerpo de la solicitud)
        nivel_alumno = request.data.get('nivel_alumno',None)

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
        

class PreguntaEditar(generics.UpdateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class PreguntaEliminar(generics.DestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class PreguntaCrear(generics.CreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
