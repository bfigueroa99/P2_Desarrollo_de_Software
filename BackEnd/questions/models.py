from django.db import models
from django.contrib.auth.models import User


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

# class Student(models.Model):
#     user_id = models.CharField(max_length=100, unique=True)
#     name = models.CharField(max_length=100)
#     level = models.FloatField(default=0.0)
#     role =  models.CharField(max_length=100)
#     mail = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Respuesta(models.Model):

    TEMAS = (
        ('Diagramas de PVT', 'Diagramas de PVT'),
        ('Calidad de mezclas', 'Calidad de mezclas'),
        ('Entalpía', 'Entalpía'),
        ('Calor latente', 'Calor latente'),
        ('Tabla de saturación', 'Tabla de saturación'),
    )
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    pregunta_relacionada = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    # estudiante = models.ForeignKey(User, on_delete=models.CASCADE)  # Supongamos que usas el modelo User de Django para los estudiantes
    respuesta_estudiante = models.CharField(max_length=255)
    uso_hint = models.BooleanField(default=False)
    respondida_correctamente = models.BooleanField(default=False)
    fecha_hora_respuesta = models.DateTimeField(auto_now_add=True)
    tipo_pregunta = models.CharField(max_length=20)  # Agrega un campo para el tipo de pregunta
    tema = models.CharField(null=True, max_length=50, choices=TEMAS)
    
    def __str__(self):
        return f'Respuesta #{self.id} a la pregunta {self.pregunta_relacionada_id} por el estudiante {self.estudiante_id}'
    




