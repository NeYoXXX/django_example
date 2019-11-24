from rest_framework import mixins
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import Province, City
from .ser import ProvinceSer
from .tools import CacheTool


class ProvinceView(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):

    queryset = Province.objects.all()
    serializer_class = ProvinceSer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        CacheTool.get_table(serializer)
        return Response(serializer.data)

