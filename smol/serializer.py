from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    item_url = serializers.ModelSerializer.serializer_url_field(
        view_name="items_detail")

    class Meta:
        model = Item
        fields = ("id", "brand", "name", "quantity", 'avg_price', 'item_url')
