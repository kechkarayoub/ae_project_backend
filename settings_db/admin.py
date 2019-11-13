# -*- coding: utf-8 -*-
from .models import SettingsDb
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin


def get_header_bg_image_preview(obj):
    if obj.header_bg:
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (str(obj.header_bg)))
    return _("No file selected!")


def get_logo_image_preview(obj):
    if obj.logo:
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (str(obj.logo)))
    return _("No file selected!")


get_header_bg_image_preview.allow_tags = True
get_header_bg_image_preview.short_description = _("Header Bg Image Preview")


get_logo_image_preview.allow_tags = True
get_logo_image_preview.short_description = _("Logo Image Preview")


class SettingsDbAdmin(TranslationAdmin):

    class Media:
        js = (
            'settings_db/js/settings_db_form.js',
        )
    list_display = ('__str__',)
    fieldsets = [
        (_("Header settings"), {
            'fields': ['site_name', 'header_bg', get_header_bg_image_preview, "logo", get_logo_image_preview]
        }),
        (_("Home page settings"), {
            'fields': [
                'home_page_title_1', 'home_page_title_2', 'home_page_left_column_title', 'home_page_left_column_p_1',
                'home_page_left_column_p_2', 'home_page_left_column_p_3', 'home_page_right_column_title',
                'home_page_right_column_p_1', 'home_page_right_column_p_2', 'home_page_right_column_p_3',
                'home_page_row_1_title', 'home_page_row_1_p_1', 'home_page_row_1_p_2', 'home_page_row_1_p_3',
                'home_page_row_2_title', 'home_page_row_2_p_1', 'home_page_row_2_p_2', 'home_page_row_2_p_3'
            ]
        }),
    ]
    readonly_fields = [get_header_bg_image_preview, get_logo_image_preview]

    def save_model(self, request, obj, form, change):
        if len(SettingsDb.objects.all()) > 0:
            SettingsDb.objects.exclude(id=obj.id).delete()
        super(SettingsDbAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request, obj=None):
        return len(SettingsDb.objects.all()) < 1


admin.site.register(SettingsDb, SettingsDbAdmin)
