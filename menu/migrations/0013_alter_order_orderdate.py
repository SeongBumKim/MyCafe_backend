# Generated by Django 3.2.7 on 2021-10-21 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_alter_order_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]