from django.urls import path, include
from rest_framework import routers
from order import views

app_name = "order"

router = routers.DefaultRouter()
router.register(r"orders", views.OrderViewSet)
router.register(r"order-items", views.OrderItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("create/", views.CreateOrderView.as_view()),
]
