# Generated by Django 5.0.6 on 2024-05-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_meow', '0006_order_lat_order_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Ожидает курьера:)', max_length=200),
        ),
    ]