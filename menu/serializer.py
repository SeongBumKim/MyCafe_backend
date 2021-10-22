from django.contrib.auth.models import User
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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        

# class UserCreateSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)
#     print(email)
#     def create(self, validated_data):
#         user = User.objects.create( # User 생성
#             email=validated_data['email'],
#             username=validated_data['username'],
#         )
#         user.set_password(validated_data['password'])

#         user.save()
#         return user