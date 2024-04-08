from rest_framework import serializers
from .models import Order, OrderDetail

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
        depth = 1  # Specify the depth to include nested representations
