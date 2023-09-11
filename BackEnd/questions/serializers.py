from rest_framework import serializers
from .models import Pregunta

class PreguntaSerializer(serializers.ModelSerializer):
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

