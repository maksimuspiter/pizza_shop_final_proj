from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import Account


class CreateUserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username="test", password="12test12")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username="wrong", password="12test12")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username="test", password="wrong")
        self.assertFalse(user is not None and user.is_authenticated)


class CreateAccountTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create_account(
            email="test@example.com", password="test"
        )
        self.account.save()

    def tearDown(self):
        self.account.delete()

    def test_account_user_data(self):
        user = User.objects.get(username="test@example.com", email="test@example.com")
        self.assertTrue(user is not None and Account.objects.first().user == user)
