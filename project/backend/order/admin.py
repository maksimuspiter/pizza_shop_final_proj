from django.contrib import admin
from .models import Order, OrderItem
from django.template.loader import get_template
from django.utils.html import mark_safe


@admin.action(description="Обновить общюю цену")
def ubdate_total_price(modeladmin, request, queryset):
    for item in queryset:
        item.update_total_price()


class OrderItemAdminInline(admin.TabularInline):
    extra = 1
    model = OrderItem
    fields = "img", "content_type", "object_id", "quantity", "price"
    readonly_fields = ("price", "img")

    def img(self, obj):
        return mark_safe(f'<img src = "{obj.get_img()}" width = "25"/>')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    fields = (
        "customer",
        "status",
        "order_items_inline",
        "total_price",
        "paid",
        "address",
    )
    readonly_fields = ("order_items_inline", "total_price")

    list_display = [
        "customer",
        "status",
        "total_price",
        "paid",
        "created",
        "updated",
        "address",
    ]
    list_filter = ["status", "paid"]
    search_fields = ["address", "customer"]
    list_editable = ["address", "status", "paid"]
    actions = [ubdate_total_price]

    def order_items_inline(self, *args, **kwargs):
        context = getattr(self.response, "context_data", None) or {}
        inline = context["inline_admin_formset"] = context["inline_admin_formsets"].pop(
            0
        )
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response
