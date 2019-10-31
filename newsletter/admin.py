# -*- coding: utf-8 -*-


from .models import Newsletter
from django.contrib import admin


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'is_active',)
    list_filter = ['is_active']
    search_fields = ['first_name', 'last_name', 'email']
    readonly_fields = ['first_name', 'last_name', 'email']


admin.site.register(Newsletter, NewsletterAdmin)
