from django.db import models
from django.db.models import Sum
from decimal import Decimal
from django.contrib.auth.models import User
from django.shortcuts import reverse
import os
from settings.settings import MEDIA_URL

SIZE = (
    ("S", "Small, 25 cm"),
    ("M", "Medium, 30 cm"),
    ("L", "Large, 35 cm"),
)


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f"/{self.slug}/"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Topping(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.slug}"

    def get_absolute_url(self):
        return f"/{self.slug}/"

    def get_price():
        pass

    class Meta:
        verbose_name = "Топпинг"
        verbose_name_plural = "Топпинги"


class BasePizza(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50)
    base_toppings = models.ManyToManyField(
        Topping, related_name="pizzas", blank=True, verbose_name="Основные топпинги"
    )
    image = models.ImageField(upload_to="uploads/pizza/", blank=True, null=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    extra_toppings = models.ManyToManyField(
        Topping, blank=True, verbose_name="Возможные дополнительные топпинги"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Основа для пиццы"
        verbose_name_plural = "Основы для пицц"

    def get_image(self):
        print("http://127.0.0.1:8000" + MEDIA_URL + "default_img/user_standart_avatar.png")
        if self.image:
            print("http://127.0.0.1:8000" + self.image.url )
            return "http://127.0.0.1:8000" + self.image.url
        return (
            "http://127.0.0.1:8000" + MEDIA_URL + "default_img/user_standart_avatar.png"
        )

    def get_middle_pizza(self):
        _middle_pizza = self.pizzas.filter(size="M", category=1).first()
        return _middle_pizza

    def get_description(self):
        description = []
        for topping in self.base_toppings.all():
            description.append(topping.title)
        return ", ".join(description)

    def get_pizza_model_name(self):
        return self.pizzas.model.__name__

    def get_price(self):
        return self.min_price


class Pizza(models.Model):
    base_pizza = models.ForeignKey(
        BasePizza, on_delete=models.CASCADE, related_name="pizzas"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=1, choices=SIZE, default="S")
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=True, blank=True, related_name="pizzas"
    )
    available = models.BooleanField(default=True)
    weight = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.base_pizza.title} {self.size} {self.category}"

    class Meta:
        verbose_name = "Пицца"
        verbose_name_plural = "Пиццы"

    def save(self, *args, **kwargs):
        self.slug = f"{self.base_pizza.slug }-{self.pk}"
        super().save(*args, **kwargs)

    def get_price(self):
        return self.price

    def get_image(self):
        return self.base_pizza.get_image()


def product_directory_path(instance, filename):
    return "uploads/{0}/{1}".format(instance.__class__.__name__.lower(), filename)


class BaseProduct(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    weight = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=product_directory_path, blank=True, null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена товара",
        blank=True,
        default=0,
    )
    available = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self._meta.verbose_name}: {self.title}, {self._meta}"

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return (
            "http://127.0.0.1:8000" + MEDIA_URL + "default_img/user_standart_avatar.png"
        )

    def get_models_name(self):
        return self.__class__.__name__

    def get_price(self):
        return self.price


class Snack(BaseProduct):
    class Meta:
        verbose_name = "Закуска"
        verbose_name_plural = "Закуски"


class Drink(BaseProduct):
    class Meta:
        verbose_name = "Напиток"
        verbose_name_plural = "Напитки"


class Desert(BaseProduct):
    class Meta:
        verbose_name = "Десерт"
        verbose_name_plural = "Десерты"


class Other(BaseProduct):
    class Meta:
        verbose_name = "Другой товар"
        verbose_name_plural = "Другие товары"
