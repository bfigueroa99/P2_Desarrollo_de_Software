from django.urls import path
from . import views

urlpatterns = [
    path('preguntas/', views.ListaPreguntas.as_view(), name='lista_preguntas'),
    path('preguntas/<int:pk>/', views.DetallePregunta.as_view(), name='detalle_pregunta'),
    path('preguntas/aleatoria/', views.PreguntaAleatoria.as_view(), name='pregunta_aleatoria'),
]
