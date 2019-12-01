# -*- coding: utf-8 -*-
from .serializers import ContactBuySerializer, ContactSellSerializer
from admin_data.models import AdminData
from backend.utils import get_list_social_links_images, send_email
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from settings_db.models import SettingsDb
from sociallink.views import get_list_social_links
import datetime


@api_view(['POST'])
def contact_sell_create(request):
    """
    Create a contact entry for selling a property.
    """
    if request.method == 'POST':
        data = request.data
        serializer = ContactSellSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "email": data['email'],
                "environment": settings.ENVIRONMENT,
                "first_name": data['first_name'],
                "last_name": data['last_name'],
                "logo_url": settings.BACKEND_URL_ROOT + static("contact/images/logo.jpg"),
                "message": data['message'],
                "site_name": SettingsDb.get_site_name(),
                "site_url_root": settings.SITE_URL_ROOT,
                "show_unsubscribe_url": True,
                "social_links": get_list_social_links(),
                "social_links_images": get_list_social_links_images(),
                "phone": data['phone']
            }
            html_content = get_template('contact/contact_template.html').render(context)
            text_content = get_template('contact/contact_template.txt').render(context)
            send_email(data["object"], text_content, data["email"], AdminData.get_admin_email(), html_content)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def contact_buy_create(request):
    """
    Create a contact entry for buying a property.
    """
    data = request.data.copy()
    if not data.get("lot_size_max", ""):
        data["lot_size_max"] = 0
        data["lot_size_min"] = 0
    if not data.get("lot_size_min", ""):
        data["lot_size_min"] = 0
    try:
        data["occupation_date"] = datetime.datetime.strptime(data.get("occupation_date"), "%d-%m-%Y").date()
    except:
        data["occupation_date"] = None
    serializer = ContactBuySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        context = {
            "email": data['email'],
            "environment": settings.ENVIRONMENT,
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "logo_url": settings.BACKEND_URL_ROOT + static("contact/images/logo.jpg"),
            "phone": data['phone'] if 'phone' in data else "",
            "property_information": [
                (_("Bathrooms number"), data['bathrooms_number_text'] if 'bathrooms_number' in data else ""),
                (_("Bedrooms number"), data['bedrooms_number_text'] if 'bedrooms_number' in data else ""),
                (_("Building type"), data['building_type_text'] if 'building_type' in data else ""),
                (_("City"), data['city_text'] if 'city' in data else ""),
                (_("Construction age"), data['construction_age_text'] if 'construction_age' in data else ""),
                (_("Dining room"), data['has_dining_room'] if 'has_dining_room' in data else ""),
                (_("Fireplace"), data['has_fireplace'] if 'has_fireplace' in data else ""),
                (_("Garage"), data['has_garage'] if 'has_garage' in data else ""),
                (_("Garden"), data['has_garden'] if 'has_garden' in data else ""),
                (_("Property size max"), str(data['lot_size_max'])
                    if 'lot_size_max' in data and int(data['lot_size_max']) > 0 else ""),
                (_("Property size min"), str(data['lot_size_min'])
                    if 'lot_size_min' in data and int(data['lot_size_min']) > 0 else ""),
                (_("Price range"), data['price_range_text'] if 'price_range' in data else ""),
                (_("Property type"), data['property_type_text'] if 'property_type' in data else ""),
                (_("Occupation date"), data['occupation_date'] if 'occupation_date' in data else ""),
                (_("Other characteristics"), data['other_characteristics'] if 'other_characteristics' in data else ""),
                (_("Status"), data['status_text'] if 'status' in data else ""),
                (_("Swimming pool"), data['has_swimming_pool'] if 'has_swimming_pool' in data else "")
            ],
            "site_name": SettingsDb.get_site_name(),
            "site_url_root": settings.SITE_URL_ROOT,
            "show_unsubscribe_url": True,
            "social_links": get_list_social_links(),
            "social_links_images": get_list_social_links_images()
        }
        html_content = get_template('contact/contact_buying_template.html').render(context)
        text_content = get_template('contact/contact_buying_template.txt').render(context)
        send_email(_("Buying property"), text_content, data["email"], AdminData.get_admin_email(), html_content)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def contact(request):
    """
    send mail from client to administrator.
    """
    if request.method == 'POST':
        data = request.data
        context = {
            "email": data['email'],
            "environment": settings.ENVIRONMENT,
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "logo_url": settings.BACKEND_URL_ROOT + static("contact/images/logo.jpg"),
            "message": data['message'],
            "site_name": SettingsDb.get_site_name(),
            "site_url_root": settings.SITE_URL_ROOT,
            "show_unsubscribe_url": True,
            "social_links": get_list_social_links(),
            "social_links_images": get_list_social_links_images(),
            "phone": data['phone'],
            "property_url": data.get('property_url', '')
        }
        html_content = get_template('contact/contact_template.html').render(context)
        text_content = get_template('contact/contact_template.txt').render(context)
        send_email(data["object"], text_content, data["email"], AdminData.get_admin_email(), html_content)
        return Response({
            "success": True
        })
