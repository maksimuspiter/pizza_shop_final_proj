from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, status, permissions, generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response

from .serializers import OrderSerializer, OrderItemSerializer, AddtocartSerializers
from .models import Order, OrderItem
from .permissions import IsOwnerOrAdmin


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrAdmin]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser]


class CreateOrderView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddtocartSerializers
    queryset = Order.objects.all()

    def create(self, serializer):
        data = {"create": True, "order_items_img": []}
        address = serializer.data.get("address")
        order_items = serializer.data.get("goods")
        order = Order.objects.create(
            customer=self.request.user.account, address=address
        )

        for item in order_items:
            content_type = item.get("content_type").lower()
            object_id = item.get("object_id")
            quantity = item.get("quantity")
            order_item = OrderItem.objects.create(
                order=order,
                content_type=ContentType.objects.get(model=content_type),
                object_id=object_id,
                quantity=quantity,
            )
            data["order_items_img"].append(order_item.get_img())
        order.update_total_price()
        data["order_id"] = order.id
        data["total_price"] = order.total_price
        return Response(data, status=status.HTTP_201_CREATED)
