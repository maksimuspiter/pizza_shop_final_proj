from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    BasePizzaSerializer,
    DesertSerializer,
    DrinkSerializer,
    OtherSerializer,
    SnackSerializer

)
from .models import BasePizza, Desert, Drink, Other, Snack


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = BasePizza.objects.all()
    serializer_class = BasePizzaSerializer
    permission_classes = []


class DesertViewSet(viewsets.ModelViewSet):
    queryset = Desert.objects.all()
    serializer_class = DesertSerializer
    permission_classes = []

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = []

class OtherViewSet(viewsets.ModelViewSet):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer
    permission_classes = []

class SnackViewSet(viewsets.ModelViewSet):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = []
