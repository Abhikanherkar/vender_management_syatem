from django.db import models
from vender.models import Vender

# Create your models here.


class PurchaseOrdeers(models.Model):
    status_choices = [
        ('Pending', "Pending"),
        ('Completed',"Completed"),
        ('Cancelled',"Cancelled"),
    ]
    po_number = models.CharField(max_length=500, unique=True)
    vender = models.ForeignKey(Vender, related_name="vender_order", on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True)
    items = models.JSONField(null=True)
    quantity = models.IntegerField(null=True)
    status = models.CharField(max_length=100, choices=status_choices, default="Pending")
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(auto_now=True)
    acknowledgment_date = models.DateTimeField(null=True)