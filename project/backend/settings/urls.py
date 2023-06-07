from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-users/", include("users.urls", namespace="users")),
    path("api-pizza/", include("pizza.urls", namespace="pizza")),
    path("api-order/", include("order.urls", namespace="order")),
    path("api-auth/", include("rest_framework.urls")),
]
