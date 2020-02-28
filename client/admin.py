# -*- coding: utf-8 -*-
from .models import Client, Leasing
from django.contrib import admin
from django.http import HttpResponseRedirect
import datetime


class ClientAdmin(admin.ModelAdmin):

    class Media:
        js = ('client/js/client_form.js',)

    fieldsets = [
        (None, {
            'fields': ['first_name', 'last_name', 'email', 'phone', 'is_active']
        }),
    ]
    list_display = ('first_name', 'last_name', 'email',)
    list_filter = ['is_active']
    ordering = ('-createdAt',)
    search_fields = ['first_name', 'last_name', 'email', 'phone']


class LeasingAdmin(admin.ModelAdmin):

    class Media:
        js = ('client/js/leasing_form.js',)

    fieldsets = [
        (None, {
            'fields': [
                'client', 'item', 'month_treated', 'payment_day', 'start_at', 'end_at', 'price', 'is_paid', 'is_active'
            ]
        }),
    ]
    list_display = ('__str__', 'is_active', 'is_paid', 'payment_day', 'price', 'start_at', 'end_at')
    list_filter = ['is_active', 'is_paid']
    ordering = ('-createdAt',)
    search_fields = ['__str__', 'month_treated']

    def changelist_view(self, request, extra_context=None):
        if not request.META['QUERY_STRING'] and \
                not request.META.get('HTTP_REFERER', '').startswith(request.build_absolute_uri()):
            return HttpResponseRedirect(request.path + "?is_paid__exact=0")
        return super(LeasingAdmin, self).changelist_view(request, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        obj.createdBy = "admin"
        super(LeasingAdmin, self).save_model(request, obj, form, change)


admin.site.register(Client, ClientAdmin)
admin.site.register(Leasing, LeasingAdmin)
