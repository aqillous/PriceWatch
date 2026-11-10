from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_current_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Current price must be a positive number.")
        return value

