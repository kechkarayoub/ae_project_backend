# -*- coding: utf-8 -*-
from .models import Testimonial
from django.contrib import admin


class TestimonialAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'contact/js/contact_buy_form.js',
        )

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'city', 'testimonial')
        }),
    )
    list_display = ('first_name', 'last_name', 'city',)
    list_filter = ['createdAt',  'city']
    search_fields = ['first_name', 'last_name', 'testimonial']
    ordering = ('-createdAt',)

    def has_add_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass


admin.site.register(Testimonial, TestimonialAdmin)
