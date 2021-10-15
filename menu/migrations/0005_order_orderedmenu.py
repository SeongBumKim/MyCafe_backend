# Generated by Django 3.2.7 on 2021-10-15 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menu_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('orderNum', models.IntegerField()),
                ('totalPrice', models.DecimalField(decimal_places=0, max_digits=10)),
                ('orderDate', models.DateField()),
                ('paymentState', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.order')),
                ('menuId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
            ],
        ),
    ]
