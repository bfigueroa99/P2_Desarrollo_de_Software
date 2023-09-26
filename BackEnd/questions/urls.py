from django.urls import path
from . import views

urlpatterns = [
    path('preguntas/', views.ListaPreguntas.as_view(), name='lista_preguntas'),
    path('preguntas/<int:pk>/', views.DetallePregunta.as_view(), name='detalle_pregunta'),
    path('api/get_random_question/', views.get_random_question, name='get_random_question'),
    path('preguntas/aleatoria/', views.PreguntaAleatoria.as_view(), name='pregunta_aleatoria'),
    path('rellenar/', views.RellenarBaseDeDatos.as_view(), name='rellenar_base_de_datos'),
    path('api/registrar_respuesta/', views.RegistrarRespuesta.as_view(), name='registrar_respuesta'),
    path('respuestas/', views.ListaRespuestas.as_view(), name='lista_respuestas'),
    path('eliminar-todas-las-respuestas/', views.EliminarTodasLasRespuestas.as_view(), name='eliminar_todas_las_respuestas'),
    path('siguiente_pregunta/', views.SiguientePregunta.as_view(), name='siguiente_pregunta'),
    path('seleccionar_primera_pregunta/', views.SeleccionarPrimeraPregunta.as_view(), name='seleccionar_primera_pregunta'),

    # Rutas de la API para cargar imágenes
    path('api/cargar_imagen/', views.ImageViewSet.as_view(), name='cargar_imagen'),
]
