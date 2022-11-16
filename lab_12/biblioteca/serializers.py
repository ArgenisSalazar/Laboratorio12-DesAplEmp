from rest_framework import serializers
from .models import Prestamos


class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamos
        fields = ('idPrestamo','idLibro', 'idUsuario', 'FecPrestamo', 'FecDevolucion')

    def create(self,validated_data):
        return Prestamos.objects.create(**validated_data)