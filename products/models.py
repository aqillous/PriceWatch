from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    image_url = models.URLField(blank=True, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    last_checked = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
