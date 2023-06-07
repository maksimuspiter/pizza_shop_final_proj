from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff"]


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ["id", "nickname", "user", "birthday", "created"]


class CreateAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Account
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        account = Account.objects.create_account(email=email, password=password)
        return account
