from rest_framework import serializers
from core.models import Guitarra, Pedido


class GuitarraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guitarra
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
