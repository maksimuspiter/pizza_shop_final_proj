from rest_framework import serializers
from .models import (
    Category,
    Pizza,
    Topping,
    BasePizza,
    BaseProduct,
    Snack,
    Drink,
    Desert,
    Other,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
        )


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = (
            "id",
            "title",
        )


class PizzaSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Pizza
        fields = ("id", "category", "price", "size", "slug")


class BasePizzaSerializer(serializers.ModelSerializer):
    options = PizzaSerializer(many=True, source='pizzas', read_only=True)
    base_toppings = ToppingSerializer(many=True)
    product_name = serializers.CharField(source="get_pizza_model_name", read_only=True)
    image_url = serializers.URLField(source="get_image")
    description = serializers.CharField(source="get_description", read_only=True)

    class Meta:
        model = BasePizza
        fields = (
            "id",
            "slug",
            "product_name",
            "title",
            "description",
            "image_url",
            "min_price",

            "base_toppings",
            "options",
        )


class BaseProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="get_models_name", read_only=True)
    image_url = serializers.URLField(source="get_image")
    min_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, source="price"
    )

    class Meta:
        model = BaseProduct
        abstract = True


class DesertSerializer(BaseProductSerializer):
    class Meta:
        model = Desert
        fields = (
            "id",
            "slug",
            "product_name",
            "title",
            "description",
            "image_url",
            "min_price",

            "weight",
        )


# class SnackSerializer(BaseProductSerializer):
#     class Meta:
#         model = Snack
#         fields = ("id", "slug", "title", "description", "weight", "get_image", "get_price")


# class DrinkSerializer(BaseProductSerializer):
#     class Meta:
#         model = Drink
#         fields = ("id", "slug", "title", "description", "weight", "get_image", "get_price")


# class OtherSerializer(BaseProductSerializer):
#     class Meta:
#         model = Other
#         fields = ("id", "slug", "title", "description", "weight", "get_image", "get_price")
