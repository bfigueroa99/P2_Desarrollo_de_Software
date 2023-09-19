from django.urls import path
from . import views

urlpatterns = [
    # path('preguntas/', views.mostrar_preguntas, name='mostrar_preguntas'),
    # path('progreso/', views.ver_progreso, name='ver_progreso'),
    # path('responder_pregunta/<int:pregunta_id>/', views.responder_pregunta, name='responder_pregunta'),
    # Agrega más URLs según tus necesidades.

    path('ver_pregunta/<int:pregunta_id>/', views.ver_pregunta, name='ver_pregunta'),
    path('crear_pregunta/', views.crear_pregunta, name='crear_pregunta'),

]
