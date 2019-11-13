# -*- coding: utf-8 -*-
from .models import Item, ItemImage
from django.conf import settings
from rest_framework import serializers


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ('pk', 'image',)

    def to_representation(self, instance):
        representation = super(ItemImageSerializer, self).to_representation(instance)
        if instance.image and instance.image.url:
            representation['image'] = settings.BACKEND_URL_ROOT + instance.image.url
        else:
            representation['image'] = ""

        return representation


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
