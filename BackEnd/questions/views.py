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

# Create your views here.
