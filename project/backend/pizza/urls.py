from django.urls import path, include
from rest_framework import routers
from pizza import views

app_name = "pizza"

router = routers.DefaultRouter()
router.register(r'pizzas', views.PizzaViewSet)
router.register(r'desert', views.DesertViewSet)
router.register(r'drink', views.DrinkViewSet)
router.register(r'other', views.OtherViewSet)
router.register(r'snack', views.SnackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
