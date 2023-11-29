from rest_framework.serializers import ModelSerializer
from purchase_orders.models import PurchaseOrdeers



class PurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrdeers
        fields = ('po_number','vender', 'order_date','items','quantity', 'delivery_date')


class PurchaseOrderRetriveSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrdeers
        fields = '__all__'