from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.
class Item(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    avg_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.name
