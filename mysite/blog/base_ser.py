from rest_framework import serializers
from .models import Province, City

class ProvinceSer(serializers.ModelSerializer):
    aa = serializers.SerializerMethodField()
    class Meta:
        model=Province
        fields = "__all__"

    def get_aa(self, inst):
        print(inst)
        ss="123456"
        return ss


class CitySer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields = "__all__"
