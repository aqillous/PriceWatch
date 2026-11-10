from django.db import models
from django.conf import settings

from products.models import Product

class TrackedProduct(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='tracked_products'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='tracking_users'
    )
    target_price = models.DecimalField(max_digits=10, decimal_places=2)
    notification_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'], 
                name='unique_user_product'
            )
        ]

    def __str__(self):
        return f"{self.user.username} tracking {self.product.name}"


class PriceHistory(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='price_history'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-recorded_at']

    def __str__(self):
        return f"{self.product.name} - {self.price} at {self.recorded_at}"
