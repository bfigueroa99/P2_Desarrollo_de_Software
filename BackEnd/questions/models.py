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

    TEMAS = (
        ('Diagramas de PVT', 'Diagramas de PVT'),
        ('Calidad de mezclas', 'Calidad de mezclas'),
        ('Entalpía', 'Entalpía'),
        ('Calor latente', 'Calor latente'),
        ('Tabla de saturación', 'Tabla de saturación'),
    )

    tema = models.CharField(null=True, max_length=50, choices=TEMAS)
    tipo = models.CharField(max_length=20, choices=TIPOS_PREGUNTA)
    nivel_dificultad = models.CharField(max_length=20, choices=NIVELES_DIFICULTAD)
    enunciado = models.TextField()
    alternativa1 = models.CharField(max_length=255, null=True, blank=True)
    alternativa2 = models.CharField(max_length=255, null=True, blank=True)
    alternativa3 = models.CharField(max_length=255, null=True, blank=True)
    alternativa4 = models.CharField(max_length=255, null=True, blank=True)
    #imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)  # Para ejercicios con imágenes
    respuesta = models.CharField(max_length=255, null=True, blank=True)  # Respuesta para preguntas de alternativas
    #imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)  # Para ejercicios con imágenes
    hint = models.TextField(null=True, blank=True)  # Campo para agregar hints
    

    def __str__(self):
        return self.enunciado
