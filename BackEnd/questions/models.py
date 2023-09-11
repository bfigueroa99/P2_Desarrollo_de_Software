from django.db import models

class Pregunta(models.Model):
    TIPOS_PREGUNTA = (
        ('alternativas', 'Pregunta de Alternativas'),
        ('calculonumerico', 'Ejercicio de Cálculo Numérico'),
    )
    
    NIVELES_DIFICULTAD = (
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    )

    tipo = models.CharField(max_length=20, choices=TIPOS_PREGUNTA)
    nivel_dificultad = models.CharField(max_length=20, choices=NIVELES_DIFICULTAD)
    enunciado = models.TextField()
    respuesta = models.CharField(max_length=255, null=True, blank=True)  # Respuesta para preguntas de alternativas
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)  # Para ejercicios con imágenes
    hint = models.TextField(null=True, blank=True)  # Campo para agregar hints

    def __str__(self):
        return self.enunciado
