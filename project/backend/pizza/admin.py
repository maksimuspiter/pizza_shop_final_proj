from django.contrib import admin
from pizza.models import (
    Pizza,
    Category,
    Topping,
    BasePizza,
    Snack,
    Drink,
    Other,
    Desert,
)


@admin.register(BasePizza)
class BasePizzaAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "min_price", "image"]
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ["min_price"]


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ["id", "price", "size", "category", "base_pizza"]
    list_filter = ["size", "category", "base_pizza"]
    list_editable = ["size", "category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


class BaseProduct(admin.ModelAdmin):
    list_display = ["id", "title", "weight", "description"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Snack)
class SnackAdmin(BaseProduct):
    pass


@admin.register(Drink)
class DrinkAdmin(BaseProduct):
    pass


@admin.register(Other)
class OtherAdmin(BaseProduct):
    pass


@admin.register(Desert)
class DesertAdmin(BaseProduct):
    pass
