from rest_framework import serializers
from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    """Serializer for Menu model"""
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    class Meta:
        model = Booking
        fields = '__all__'
