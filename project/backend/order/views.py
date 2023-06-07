from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, status, permissions, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .serializers import OrderSerializer, OrderItemSerializer, AddtocartSerializers
from .models import Order, OrderItem
from .permissions import IsOwnerOrAdmin


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrAdmin]
    authentication_classes = [TokenAuthentication]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


class CreateOrderView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    queryset = OrderItem.objects.all()
    serializer_class = AddtocartSerializers

    def perform_create(self, serializer):
        data = {
            "create": True,
        } 
        address = serializer.data.get("address")
        order_items = serializer.data.get("goods")
        order = Order.objects.create(
            customer=self.request.user.account, address=address
        )
        for item in order_items:
            content_type = item.get("content_type").lower()
            object_id = item.get("object_id")
            quantity = item.get("quantity")
            order_items = OrderItem.objects.create(
                order=order,
                content_type=ContentType.objects.get(model=content_type),
                object_id=object_id,
                quantity=quantity,
            )
        order.update_total_price()
        data['order_id'] = order.id
        
        return Response(data, status=status.HTTP_201_CREATED)
