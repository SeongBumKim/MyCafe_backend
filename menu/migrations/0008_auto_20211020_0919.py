# Generated by Django 3.2.7 on 2021-10-20 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_remove_order_paymentstate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderedmenu',
            old_name='OrderId',
            new_name='orderId',
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
