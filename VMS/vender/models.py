from django.db import models

# Create your models here.


class Vender(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField()
    address = models.TextField()
    vender_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField( null=True)
    avg_response_time = models.FloatField(null=True)
    fulfillement_rate = models.FloatField(null=True)