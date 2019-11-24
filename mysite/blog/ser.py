from rest_framework import serializers
from .models import Province, City

class ProvinceSer(serializers.ModelSerializer):
    class Meta:
        model=Province
        fields = "__all__"


class CitySer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields = "__all__"
