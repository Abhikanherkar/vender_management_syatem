# Generated by Django 4.2.7 on 2023-11-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0002_alter_purchaseordeers_delivery_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseordeers',
            name='completed_date',
            field=models.DateTimeField(null=True),
        ),
    ]