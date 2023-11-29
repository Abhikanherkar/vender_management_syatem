from rest_framework.serializers import ModelSerializer

from vender.models import Vender



class VenderSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Vender


class VenderSerializerForUpdate(ModelSerializer):
    class Meta:
        fields = ('name', 'contact_details', 'address', 'vender_code')
        model = Vender