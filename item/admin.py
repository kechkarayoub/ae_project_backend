# -*- coding: utf-8 -*-
from .models import ItemImage, Item
from backend.utils import generate_id
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from easy_select2 import select2_modelform
from modeltranslation.admin import TranslationAdmin


ItemForm = select2_modelform(Item, attrs={'width': '250px'})


def get_item_images_preview(obj):
    if obj.image:
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (str(obj.image)))
    return _("No file selected!")


def get_item_image_map_preview(obj):
    if obj.image_map:
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (str(obj.image_map)))
    return _("No file selected!")


get_item_images_preview.allow_tags = True
get_item_images_preview.short_description = _("Image Preview")

get_item_image_map_preview.allow_tags = True
get_item_image_map_preview.short_description = _("Image Preview")


class ItemImagesInline(admin.StackedInline):
    model = ItemImage
    extra = 0
    fields = ['image', get_item_images_preview]
    readonly_fields = [get_item_images_preview]


class ItemAdmin(TranslationAdmin):

    class Media:
        js = (
            'item/js/item_form.js',
        )
    form = ItemForm
    list_display = (
        'item_id', 'city', 'property_type', 'building_type', 'price', 'lot_size', 'status', 'bedrooms_number',
        'bathrooms_number', 'is_active',
    )
    fieldsets = [
        (_("General information"), {
            'fields': ['label', 'short_description', 'description', 'address', 'city', 'price']
        }),
        (_("Characteristics"), {
            'fields': [
                'annual_income', 'bedrooms_number', 'bathrooms_number', 'building_type', 'ccd', 'construction_age',
                'cost_per_housing', 'down_payment_required', 'economic_value', 'gross_revenue_multiplier',
                'property_type', 'apartments_number', 'housing_descriptions', 'has_dining_room', 'has_fireplace',
                'has_garage', 'has_swimming_pool', 'has_garden', 'lot_size', 'maximum_loan', 'net_income_multiplier',
                'overall_rate_update', 'catalog'
            ]
        }),
        (_("Added fields"), {
            'fields': [
                'added_field_1_label', 'added_field_1_value', 'added_field_2_label', 'added_field_2_value',
                'added_field_3_label', 'added_field_3_value',
            ]
        }),
        (_("Map options"), {
            'fields': ['with_map', 'gps_latitude', 'gps_longitude', ('image_map', get_item_image_map_preview,)]
        }),
        (None, {
            'fields': ['status', 'is_active']
        }),
    ]
    inlines = [ItemImagesInline]
    list_filter = [
        'apartments_number', 'bathrooms_number', 'bedrooms_number', 'building_type', 'construction_age', 'createdAt',
        'has_dining_room', 'has_fireplace', 'has_garage', 'has_garden', 'has_swimming_pool', 'is_active', 'lot_size',
        'price', 'property_type', 'status', 'with_map'
    ]
    search_fields = ['address', 'description', 'label', 'housing_descriptions', 'short_description']
    readonly_fields = [get_item_image_map_preview]

    def save_model(self, request, obj, form, change):
        if not obj.item_id:
            try:
                last_id = Item.objects.latest('createdAt').item_id
            except Item.DoesNotExist:
                last_id = None
            obj.item_id = generate_id(last_id)
        super(ItemAdmin, self).save_model(request, obj, form, change)


admin.site.register(Item, ItemAdmin)
