from rest_framework import serializers

from menu.models import Menu


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'stocked','category','imgUrl']

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'stocked','category','imgUrl']
