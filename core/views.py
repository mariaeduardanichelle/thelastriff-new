from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.models import Guitarra, Pedido
from core.serializers import GuitarraSerializer, PedidoSerializer


class GuitarraViewSet(ModelViewSet):
    queryset = Guitarra.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GuitarraSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PedidoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]