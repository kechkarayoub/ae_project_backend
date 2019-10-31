# -*- coding: utf-8 -*-
from .models import Item
from modeltranslation.translator import translator, TranslationOptions


class ItemTranslationOptions(TranslationOptions):
    fields = ('address', 'description', 'label', 'short_description', )


translator.register(Item, ItemTranslationOptions)