# -*- coding: utf-8 -*-
from .models import Testimonial
from django.utils.translation import get_language
from rest_framework import serializers
import locale


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = (
            'city', 'city_val', 'createdAt', 'first_name', 'initials_bg_color', 'initials_color', 'last_name', 'pk',
            'testimonial'
        )

    def to_representation(self, instance):
        representation = super(TestimonialSerializer, self).to_representation(instance)
        current_language = get_language()
        if current_language == "fr":
            try:
                locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
            except:
                try:
                    locale.setlocale(locale.LC_ALL, "fr")
                except:
                    pass

            representation['createdAt'] = instance.createdAt.strftime("%d %B, %Y")
        else:
            representation['createdAt'] = instance.createdAt.strftime("%B %d, %Y")

        return representation
