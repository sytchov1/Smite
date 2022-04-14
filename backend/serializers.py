from rest_framework.serializers import ModelSerializer
from .models import WowClass, Weapon


class WowClassSerializer(ModelSerializer):
    class Meta:
        model = WowClass
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'