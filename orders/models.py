from django.db import models

from customers.models import Customer
from robots.models import Robot


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="orders")
    robot = models.ForeignKey(Robot,on_delete=models.CASCADE, related_name="orders")
