from rest_framework import serializers

from menu.models import Menu, Order, OrderedMenu


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'stocked', 'category', 'imgUrl', 'ordered']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'orderNum', 'totalPrice', 'orderDate', 'paymentState']


class OrderedMenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderedMenu
        fields = ['MenuId', 'OrderId']




