from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Order
from .kafka_producers import send_order_event


class OrderCreateView(APIView):
    def post(self,request):
        user = request.data.get("user")
        item = request.data.get("item")
        order = Order.objects.create(user=user,item=item)

        send_order_event({
            "order_id":order.id,
            "user":user,
            "item":item ,
            "status" : order.status
        })

        return Response({"message":"Order placed successfully!"},status=status.HTTP_201_CREATED)