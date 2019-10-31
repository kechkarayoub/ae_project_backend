# -*- coding: utf-8 -*-
from .models import Contact, ContactBuy
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):

    class Media:
        js = ('contact/js/contact_form.js',)

    list_display = ('first_name', 'last_name', 'object', 'email',)
    list_filter = ['createdAt']
    ordering = ('-createdAt',)
    search_fields = ['first_name', 'last_name', 'object', 'email']

    def has_add_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass


class ContactBuyAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'contact/js/contact_buy_form.js',
        )

    list_display = ('first_name', 'last_name', 'email',)
    list_filter = ['createdAt',  'has_dining_room', 'has_fireplace', 'has_garage', 'has_swimming_pool', 'has_garden']
    ordering = ('-createdAt',)
    search_fields = ['first_name', 'last_name', 'email']

    def has_add_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactBuy, ContactBuyAdmin)
