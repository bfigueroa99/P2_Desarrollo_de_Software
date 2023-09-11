from django.contrib import admin
from .models import Pregunta

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'nivel_dificultad', 'enunciado')  # Esto es opcional, define qué campos se muestran en la lista de preguntas
