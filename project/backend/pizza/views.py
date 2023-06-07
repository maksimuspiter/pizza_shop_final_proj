from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    BasePizzaSerializer,
    DesertSerializer,
)
from .models import BasePizza, Desert


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = BasePizza.objects.all()
    serializer_class = BasePizzaSerializer
    permission_classes = []


class DesertViewSet(viewsets.ModelViewSet):
    queryset = Desert.objects.all()
    serializer_class = DesertSerializer
    permission_classes = []
