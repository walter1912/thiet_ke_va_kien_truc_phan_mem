from rest_framework import generics
from .models import Cart, CartItem
from .serializers import CartSerializer

class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = Cart.objects.filter(user=user)
    #     return queryset

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
