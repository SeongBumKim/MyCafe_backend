# Generated by Django 3.2.7 on 2021-10-21 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_alter_order_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.CharField(max_length=200),
        ),
    ]
