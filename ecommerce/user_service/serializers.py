from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 
        'address', 'phone', 'created_at', 'updated_at']
        # fields = '__all__'