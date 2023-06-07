from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "users"

router = routers.DefaultRouter()
# router.register(r'users', views.AccountViewSet, basename='user')
router.register(r"users", views.AccountViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("registrations/", views.RegistrAccountView.as_view(), name="registrations"),
]
urlpatterns += staticfiles_urlpatterns()
