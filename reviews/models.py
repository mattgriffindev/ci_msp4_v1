from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=80, null=True, blank=True)
    title = models.CharField(max_length=80, null=True)
    body = models.TextField()
    rate_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    rating = models.IntegerField(choices=rate_choices, default='0')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.product.name
