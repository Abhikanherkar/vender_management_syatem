# Generated by Django 4.2.7 on 2023-11-29 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseordeers',
            name='delivery_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='purchaseordeers',
            name='order_date',
            field=models.DateTimeField(),
        ),
    ]
