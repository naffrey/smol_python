from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.ModelSerializer.serializer_url_field(
        view_name="item_detail")

    class Meta:
        model = Item
        fields = ("id", "brand", "name", "quantity", 'avg_price')
