from rest_framework import serializers
from .models import Weapon


# class WeaponSerializer(serializers.Serializer):
#     power = serializers.IntegerField()
#     rerity = serializers.CharField()


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id', 'power', 'rerity']
