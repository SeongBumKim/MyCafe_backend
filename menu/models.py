from django.db import models
from datetime import datetime
# Create your models here.
from django.db.models import BooleanField


class Menu(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stocked = BooleanField(default=True)
    category = models.CharField(max_length=100)
    imgUrl = models.CharField(max_length=200)
    ordered = BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=200)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=0)
    orderDate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class OrderedMenu(models.Model):
    objects = models.Manager()
    menuId = models.ForeignKey(Menu, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.OrderId
