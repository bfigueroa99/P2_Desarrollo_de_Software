# models.py
from django.db import models

class Opcion(models.Model):
    texto = models.CharField(max_length=200)
    es_correcta = models.BooleanField(default=False)

class Pregunta(models.Model):
    enunciado = models.TextField()
    imagen = models.ImageField(upload_to='preguntas/')
    opciones = models.ManyToManyField(Opcion)




# class Concepto(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()

#     def __str__(self):
#         return self.nombre

# class PreguntaAlternativa(models.Model):
#     concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
#     enunciado = models.TextField()
#     alternativa_correcta = models.CharField(max_length=100)
#     alternativa_incorrecta1 = models.CharField(max_length=100)
#     alternativa_incorrecta2 = models.CharField(max_length=100)

#     def __str__(self):
#         return self.enunciado

# class EjercicioCalculo(models.Model):
#     concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
#     enunciado = models.TextField()
#     diagrama = models.ImageField(upload_to='ejercicios/')  # Asegúrate de configurar correctamente el almacenamiento de archivos estáticos.
#     respuesta = models.FloatField()
#     unidades_respuesta = models.CharField(max_length=50)
#     tolerancia = models.FloatField()  # Tolerancia para la respuesta numérica

#     def __str__(self):
#         return self.enunciado

# class EstadoEstudiante(models.Model):
#     estudiante = models.ForeignKey(User, on_delete=models.CASCADE)  # Asociar con el modelo de usuario de Django si aún no lo has hecho.
#     concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
#     puntuacion = models.FloatField()  # Puntuación del estudiante en este concepto (de 0 a 10)
#     ultima_tarea_realizada = models.DateTimeField(auto_now=True)
#     avanzado = models.BooleanField(default=False)  # Indica si el estudiante ha avanzado en este concepto

#     def __str__(self):
#         return f"{self.estudiante.username} - {self.concepto.nombre}"
