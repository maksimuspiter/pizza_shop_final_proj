from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import exceptions

from .serializers import AccountSerializer, CreateAccountSerializer
from .models import Account, EmailAlreadyExist
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes


class AccountViewSet(viewsets.ViewSet):
    queryset = Account.objects.all()

    def list(self, request):
        if request.user.is_superuser:
            serializer = AccountSerializer(self.queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=403)

    def retrieve(self, request, pk=None):
        queryset = Account.objects.all()

        if request.user.is_authenticated:
            account = get_object_or_404(self.queryset, pk=pk)
            if request.user.is_superuser or request.user.account == account:
                serializer = AccountSerializer(account)
                return Response(serializer.data)
        return Response(status=403)


class RegistrAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CreateAccountSerializer(data=request.data)
        data = {
            "create": False,
        }

        if serializer.is_valid():
            try:
                account = serializer.save()
                nickname = request.data.get("nickname")
                account.nickname = nickname
                account.save()

                data["create"] = True
                data["nickname"] = nickname
                data["email"] = account.user.email

                token = Token.objects.create(user=account.user)
                data["token"] = token.key
                return Response(data, status=status.HTTP_201_CREATED)

            except EmailAlreadyExist as e:
                data["error"] = e.message
                return Response(data, status=status.HTTP_304_NOT_MODIFIED)
        else:
            data["error"] = serializer.errors
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)


@authentication_classes([])
class LoginAccountObtainAuthToken(ObtainAuthToken):
    pass
