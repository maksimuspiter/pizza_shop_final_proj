from rest_framework import serializers
from .models import Order, OrderItem
from users.serializers import AccountSerializer
from pizza.models import Pizza, Desert, Snack, Drink, Other
from pizza.serializers import (
    PizzaSerializer,
    DesertSerializer,
    DrinkSerializer,
    SnackSerializer,
    OtherSerializer,
)


class OrderItemsObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        match value:
            case Pizza():
                serializer = PizzaSerializer(value)
            case Desert():
                serializer = DesertSerializer(value)
            case Snack():
                serializer = SnackSerializer(value)
            case Drink():
                serializer = DrinkSerializer(value)
            case Other():
                serializer =OtherSerializer(value)
            case _:
                raise Exception("Unexpected type of tagged object")

        return serializer.data


class OrderItemSerializer(serializers.ModelSerializer):
    product_data = OrderItemsObjectRelatedField(read_only=True, source="item")

    price = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "content_type",
            "object_id",
            "quantity",
            "price",
            "product_data",
        )


class OrderSerializer(serializers.ModelSerializer):
    customer = AccountSerializer(read_only=True)
    goods = OrderItemSerializer(read_only=True, many=True, source="items")
    # total_price = serializers.DecimalField(
    #     read_only=True, max_digits=10, decimal_places=2, default=0
    # )
    status = serializers.CharField(read_only=True)

    # max_digits=10, decimal_places=2,
    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "address",
            "goods",
            "created",
            "updated",
            "status",
            "total_price",
            "paid",
        )


class GoodInCartSerializer(serializers.Serializer):
    content_type = serializers.CharField(max_length=200)
    object_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)


class AddtocartSerializers(serializers.ModelSerializer):
    goods = GoodInCartSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "address", "goods")
