from rest_framework import serializers
from .models import Cart, CartItem
from user_service.serializers import UserSerializer
from book_service.serializers import BookSerializer

class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'book', 'quantity', 'created_at', 'updated_at']

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'updated_at', 'cart_items']
