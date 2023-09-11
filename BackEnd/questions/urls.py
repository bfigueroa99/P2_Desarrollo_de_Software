from django.urls import path
from . import views

urlpatterns = [
    path('preguntas/', views.ListaPreguntas.as_view(), name='lista_preguntas'),
    path('preguntas/<int:pk>/', views.DetallePregunta.as_view(), name='detalle_pregunta'),
    path('api/get_random_question/', views.get_random_question, name='get_random_question'),
]
