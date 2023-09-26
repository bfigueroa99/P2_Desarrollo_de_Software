from rest_framework import serializers
from .models import Pregunta, Respuesta, Image

class PreguntaSerializer(serializers.ModelSerializer):
    imagen_svg = serializers.ImageField(required=False)  # Asegúrate de que se permita cargar la imagen
    class Meta:
        model = Pregunta
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['tipo'] == 'alternativas':
            data['alternativa2'] = instance.alternativa2
            data['alternativa3'] = instance.alternativa3
            data['alternativa4'] = instance.alternativa4
        return data

class RespuestaSerializer(serializers.ModelSerializer):
    pregunta_relacionada = serializers.PrimaryKeyRelatedField(queryset=Pregunta.objects.all())

    class Meta:
        model = Respuesta
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

