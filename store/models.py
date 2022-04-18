from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products',null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]


class Order(models.Model):
    phone_number = models.CharField(max_length=15)
    customer_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    Address = models.CharField(max_length=500)
    date_ordered = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-date_ordered"]