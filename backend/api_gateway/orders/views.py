# views.py
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Order
from .kafka_producers import send_order_event
from .serializers import OrderSerializer

class OrderListCreateView(APIView):
    
    def get(self, request):
        orders = Order.objects.all().order_by('-created_at')  # recent first
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data.get("user")
        item = request.data.get("item")
        order = Order.objects.create(user=user, item=item)

        send_order_event({
            "order_id": order.id,
            "user": user,
            "item": item,
            "status": order.status
        })

        return Response({"message": "Order placed successfully!"}, status=status.HTTP_201_CREATED)
