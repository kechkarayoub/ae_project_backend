# -*- coding: utf-8 -*-
from .models import Item, ItemImage
from rest_framework import serializers


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ('pk', 'image',)


class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = (
            'pk', 'address', 'bedrooms_number', 'bathrooms_number', 'building_type', 'city', 'construction_age',
            'description', 'gps_latitude', 'gps_longitude', 'has_dining_room', 'has_fireplace', 'has_garage',
            'has_garden', 'has_swimming_pool', 'image_map', 'images', 'is_active', "is_new", 'label', 'lot_size',
            'property_type','price', 'short_description', 'status', 'with_map'
        )
