# Generated by Django 4.2.7 on 2023-11-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vender_code', models.CharField(max_length=100, unique=True)),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('avg_response_time', models.FloatField()),
                ('fulfillement_rate', models.FloatField()),
            ],
        ),
    ]
