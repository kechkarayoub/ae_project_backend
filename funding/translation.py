# -*- coding: utf-8 -*-
from .models import Funding
from modeltranslation.translator import translator, TranslationOptions


class FundingTranslationOptions(TranslationOptions):
    fields = (
        'description',
    )


translator.register(Funding, FundingTranslationOptions)
