from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from users.models import Account, EmailAlreadyExist
from users.views import AccountViewSet


class AccountRegistrationTests(APITestCase):
    def test_create_account_correct_data(self):
        url = reverse("users:registrations")
        data = {"email": "test@example.com", "password": "secret"}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(Account.objects.get().user, user)

    def test_create_account_with_not_unique_email(self):
        Account.objects.create_account(email="test@example.com", password="secret")
        url = reverse("users:registrations")
        data = {"email": "test@example.com", "password": "secret"}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_304_NOT_MODIFIED)

    def test_create_account_invalid_email(self):
        url = reverse("users:registrations")
        data = {"email": "test", "password": "secret"}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)


class AccountLoginTests(APITestCase):
    def test_get_token(self):
        account = Account.objects.create_account(
            email="test@example.com", password="secret"
        )

        url = reverse("users:login")
        data = {"username": "test@example.com", "password": "secret"}
        user = account.user
        token, created = Token.objects.get_or_create(user=user)
        self.assertEqual(created, True)

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, {"token": token.key})


class AccountViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test_user", email="test_user@example.com"
        )
        self.user.set_password("password")
        self.user.save()

        self.admin = User.objects.create_superuser(
            username="test_admin", email="test_admin@example.com", password="secret"
        )
        Account.objects.create(user=self.user, nickname="SimpleUser")
        Account.objects.create(user=self.admin, nickname="TheBestUser")
        self.client = APIClient()

    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.admin.delete()

    def test_get_list_by_admin(self):
        self.client.login(username="test_admin", password="secret")
        response = self.client.get("/api-users/users/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_list_by_simple_user(self):
        self.client.login(username="test_user", password="secret")
        response = self.client.get("/api-users/users/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_retrieve_by_admin(self):
        new_account = Account.objects.create_account(
            email="new_useer@example.com", password="secret"
        )

        self.client.login(username="test_admin", password="secret")
        response = self.client.get(f"/api-users/users/{new_account.pk}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_retrieve_by_simple_user(self):
        new_account = Account.objects.create_account(
            email="new_useer@example.com", password="secret"
        )

        self.client.login(username="test_user", password="secret")
        response = self.client.get(f"/api-users/users/{new_account.pk}/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_retrieve_by_owner(self):
        new_account = Account.objects.create_account(
            email="new_useer@example.com", password="secret"
        )

        self.client.login(username="new_useer@example.com", password="secret")
        response = self.client.get(f"/api-users/users/{new_account.pk}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
