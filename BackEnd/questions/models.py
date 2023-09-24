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
    imagen_svg = models.FileField(upload_to='preguntas_svg/', blank=True, null=True)
    
    

    def __str__(self):
        return self.enunciado

class Respuesta(models.Model):
    pregunta_relacionada = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    # estudiante = models.ForeignKey(User, on_delete=models.CASCADE)  # Supongamos que usas el modelo User de Django para los estudiantes
    respuesta_estudiante = models.CharField(max_length=255)
    hint_utilizado = models.BooleanField(default=False)
    respondida_correctamente = models.BooleanField(default=False)
    fecha_hora_respuesta = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Respuesta #{self.id} a la pregunta {self.pregunta_relacionada_id} por el estudiante {self.estudiante_id}'
    



