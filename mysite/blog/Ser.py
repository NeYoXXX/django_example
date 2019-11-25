from rest_framework import serializers
from .models import Place,Restaurant


class PlaceSer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class RestaurantSer(PlaceSer):
    class Meta:
        model = Restaurant
        fields = "__all__"