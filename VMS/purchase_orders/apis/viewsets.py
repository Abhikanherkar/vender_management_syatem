from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from purchase_orders.apis.serializers import PurchaseOrderSerializer
from purchase_orders.apis.serializers import PurchaseOrderRetriveSerializer

from purchase_orders.models import PurchaseOrdeers


class PurchaseOrdeerViewSet(ModelViewSet):
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrdeers.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vender']


    def get_serializer_class(self):

        if self.action in ['create', 'update']:
            return PurchaseOrderSerializer
        
        if self.action in ['list', 'retrieve']:
            return PurchaseOrderRetriveSerializer
        
        return super().get_serializer_class()