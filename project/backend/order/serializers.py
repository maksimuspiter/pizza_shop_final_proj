from rest_framework import serializers
from .models import Order, OrderItem
from users.serializers import AccountSerializer
from pizza.models import Pizza, Desert, Snack, Drink, Other
from pizza.serializers import PizzaSerializer, DesertSerializer


class OrderItemsObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Pizza):
            serializer = PizzaSerializer(value)

        elif isinstance(value, Desert):
            serializer = DesertSerializer(value)

        # elif isinstance(value, Snack):
        #     serializer =
        # elif isinstance(value, Drink):
        #     serializer =
        # elif isinstance(value, Other):
        #     serializer =

        else:
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


class AddtocartSerializers(serializers.Serializer):
    address = serializers.CharField(max_length=200)
    goods = GoodInCartSerializer(many=True)
