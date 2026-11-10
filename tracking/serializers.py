from rest_framework import serializers
from .models import PriceHistory, TrackedProduct

class TrackedProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name' , read_only=True)
    current_price = serializers.DecimalField(source='product.current_price', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = TrackedProduct
        fields = "__all__"
        read_only_fields = ["user", "product_name", "current_price", "created_at"]

    def validate_target_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Target price must be a positive number.")
        return value

    def validate(self, attrs):
       request = self.context["request"]
       product = attrs.get("product")
       if self.instance is None and product is not None:
           if TrackedProduct.objects.filter(user=request.user, product=product).exists():
               raise serializers.ValidationError({"product": "You are already tracking this product."})
       return attrs

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = ["id", "price", "recorded_at"]