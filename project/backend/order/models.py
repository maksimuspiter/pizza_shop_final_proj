from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import Account

STATUS = (
    ("DRAFT", "Черновик"),
    ("NOPAID", "Ждет оплаты"),
    ("PAID", "Оплачен"),
    ("DELIVERY", "У курьера"),
    ("DONE", "У клиента"),
    ("CHECKOUT", "На кассе"),
    ("PROBLEMS", "Проблемы с заказом"),
)


class Order(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)

    address = models.CharField(
        max_length=250, help_text="введите адрес", verbose_name="адрес"
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default="DRAFT")

    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.id}: {self.customer.user.email}-{self.status}"

    def update_total_price(self):
        self.total_price = sum(item.price for item in self.items.all())
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE, verbose_name="Заказ"
    )

    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": ("pizza", "snack", "drink", "desert", "other")},
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()

    item = GenericForeignKey("content_type", "object_id")
    quantity = models.IntegerField(verbose_name="Количество", default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Цена товара", blank=True
    )

    class Meta:
        verbose_name = "Товары в заказе"
        verbose_name_plural = "Товары в заказах"

    def save(self, *args, **kwargs):
        self.price = self.item.get_price() * self.quantity
        super().save(*args, **kwargs)

    def get_img(self):
        return self.item.get_image()
