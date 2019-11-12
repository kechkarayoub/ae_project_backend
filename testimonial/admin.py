# -*- coding: utf-8 -*-
from .models import Testimonial
from backend.utils import generate_random_color
from django.contrib import admin


class TestimonialAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'contact/js/contact_buy_form.js',
        )

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'city', 'testimonial', 'image')
        }),
    )
    list_display = ('first_name', 'last_name', 'city',)
    list_filter = ['createdAt',  'city']
    search_fields = ['first_name', 'last_name', 'testimonial']
    ordering = ('-createdAt',)

    def save_model(self, request, obj, form, change):
        color, complementary_color = generate_random_color(with_complementary=True)
        obj.initials_color = color
        obj.initials_bg_color = complementary_color
        super(TestimonialAdmin, self).save_model(request, obj, form, change)


admin.site.register(Testimonial, TestimonialAdmin)
