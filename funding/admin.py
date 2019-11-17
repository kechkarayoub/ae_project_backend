# -*- coding: utf-8 -*-
from .models import Funding
from backend.utils import generate_random_color
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe


def get_user_image_preview(obj):
    if obj.image:
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (str(obj.image)))
    return _("No file selected!")


get_user_image_preview.allow_tags = True
get_user_image_preview.short_description = _("Image Preview")


class FundingAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'funding/js/funding_form.js',
        )

    fieldsets = (
        (None, {
            'fields': ('city', 'description_en', 'description_fr', 'first_name', 'last_name', 'image', get_user_image_preview,)
        }),
    )
    list_display = ('first_name', 'last_name', 'city',)
    list_filter = ['createdAt',  'city']
    search_fields = ['first_name', 'last_name', 'description']
    ordering = ('-createdAt',)
    readonly_fields = [get_user_image_preview]

    def save_model(self, request, obj, form, change):
        color, complementary_color = generate_random_color(with_complementary=True)
        obj.initials_color = color
        obj.initials_bg_color = complementary_color
        super(FundingAdmin, self).save_model(request, obj, form, change)


admin.site.register(Funding, FundingAdmin)