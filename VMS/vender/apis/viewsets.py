from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from vender.apis.serializer import VenderSerializer
from vender.apis.serializer import VenderSerializerForUpdate
from vender.models import Vender


class VenderViewSet(ModelViewSet):
    serializer_class = VenderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Vender.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return VenderSerializerForUpdate
        return super().get_serializer_class()

