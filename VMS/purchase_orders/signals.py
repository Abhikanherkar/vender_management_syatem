import datetime
from django.db.models import F
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from purchase_orders.models import PurchaseOrdeers



@receiver(post_save, sender = PurchaseOrdeers)
def calculate_vender_matrix(created, instance, **kwargs):
    if not created:
        if instance.status == 'Completed':
            vender_instance = instance.vender
            total_orders = instance.vender.vender_order.all()
            total_orders.filter(pk = instance.pk).update(completed_date = datetime.datetime.now())
            completed_on_time = total_orders.filters(status = 'Completed', completed_date__lte = F('delivery_date'))

            quality_rating = total_orders.filter(status = 'Completed').aggregate(Avg('quality_rating'))['quality_rating__avg']
            avg_resonse_time = total_orders.annonate(date_diff = F('issue_date') - F('acknowledgment_date')).aggregate(Avg('date_diff'))["date_diff__avg"]
            
            
            vender_instance.quality_rating_avg = quality_rating
            vender_instance.avg_response_time = avg_resonse_time

            try:
                on_time_deliveery_rate = completed_on_time.count() / total_orders.filter(status = 'Completed').count()
                vender_instance.on_time_delivery_rate = on_time_deliveery_rate

            except Exception as e:
                if isinstance(e, ZeroDivisionError):
                    pass
                else:
                    raise e
                

            try:
                fulfilment_rate = total_orders.count() /  total_orders.filter(status = 'Completed').count()
                vender_instance.fulfillement_rate = fulfilment_rate

            except Exception as e:
                if isinstance(e, ZeroDivisionError):
                    pass
                else:
                    raise e
            vender_instance.save()

