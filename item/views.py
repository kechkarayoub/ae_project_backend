# -*- coding: utf-8 -*-


from .models import Item
from .serializers import ItemSerializer
from app.project_conf import NBR_ITEMS_PER_PAGE
from app.static_variables import PRICES_RANGES_VALUES
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.utils.translation import ugettext as _
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


@api_view(['GET'])
def items_list(request):
    """
    List items.
    """
    kwargs = {}
    bathrooms_number = request.GET.get("bathrooms_number", "")
    bedrooms_number = request.GET.get("bedrooms_number", "")
    building_type = request.GET.get("building_type", "")
    city = request.GET.get("city", "")
    construction_age = request.GET.get("construction_age", "")
    has_dining_room = request.GET.get("has_dining_room", "")
    has_garage = request.GET.get("has_garage", "")
    has_garden = request.GET.get("has_garden", "")
    has_fireplace = request.GET.get("has_fireplace", "")
    has_swimming_pool = request.GET.get("has_swimming_pool", "")
    item_status = request.GET.get("item_status", "")
    property_type = request.GET.get("property_type", "")
    price_range = request.GET.get("price_range", "")
    searched_txt = request.GET.get("searched_txt", "")
    if bathrooms_number:
        kwargs["bathrooms_number"] = bathrooms_number
    if bedrooms_number:
        kwargs["bedrooms_number"] = bedrooms_number
    if building_type:
        kwargs["building_type"] = building_type
    if city:
        kwargs["city"] = city
    if construction_age:
        kwargs["construction_age"] = construction_age
    if has_dining_room != "":
        kwargs["has_dining_room"] = json.loads(has_dining_room.lower())
    if has_fireplace != "":
        kwargs["has_fireplace"] = json.loads(has_fireplace.lower())
    if has_garage != "":
        kwargs["has_garage"] = json.loads(has_garage.lower())
    if has_garden != "":
        kwargs["has_garden"] = json.loads(has_garden.lower())
    if has_swimming_pool != "":
        kwargs["has_swimming_pool"] = json.loads(has_swimming_pool.lower())
    if item_status:
        kwargs["status"] = item_status
    if price_range:
        min_max = PRICES_RANGES_VALUES[price_range]
        kwargs["price__gte"] = min_max["min"]
        kwargs["price__lte"] = min_max["max"]
    if property_type:
        kwargs["property_type"] = property_type
    items = Item.objects.filter(
        Q(address__contains=searched_txt) |
        Q(description__contains=searched_txt) |
        Q(label__contains=searched_txt) |
        Q(short_description__contains=searched_txt)
    ).distinct().filter(is_active=True, **kwargs).exclude(status="sold").order_by('-createdAt')
    page = int(request.GET.get('current_page', 0)) + 1
    paginator = Paginator(items, NBR_ITEMS_PER_PAGE)
    try:
        data = paginator.page(page)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    serializer = ItemSerializer(data, context={'request': request}, many=True)
    # if data.has_next():
    #     next_page = data.next_page_number()
    # else:
    #     next_page = 0
    # if data.has_previous():
    #     previous_page = data.previous_page_number()
    # else:
    #     previous_page = 0

    return Response({
        'current_page': page,
        'count': paginator.count,
        'data': serializer.data,
        'numpages': paginator.num_pages
        # 'nextLink': '/api/items/?page=' + str(next_page) if next_page else '',
        # 'prevLink': '/api/items/?page=' + str(previous_page) if previous_page else ''
    })


@api_view(['GET'])
def item_details(request, pk):
    try:
        item = Item.objects.get(pk=pk, is_active=True)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, context={'request': request})
    return Response(serializer.data)

from app.added_settings import SITE_NAME, SITE_URL_ROOT, BACKEND_URL_ROOT
from app.utils import get_list_social_links_images
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mass_mail, EmailMultiAlternatives
from django.template.loader import get_template
from email.mime.image import MIMEImage
from newsletter.models import Newsletter
from sociallink.views import get_list_social_links

def on_transaction_commit(func):
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))

    return inner

@receiver(post_save, sender=Item)
@on_transaction_commit
def send_new_property_to_newsletters(sender, **kwargs):
    new_item = kwargs['instance']
    new_item_data = ItemSerializer(new_item).data
    images_items = new_item.images.all()
    context = {
        "logo_url": BACKEND_URL_ROOT + static("contact/images/logo.png"),
        "social_links": get_list_social_links(),
        "social_links_images": get_list_social_links_images(),
        "site_name": SITE_NAME,
        "site_url_root": SITE_URL_ROOT,
        "backend_url": BACKEND_URL_ROOT,
        "property_label": new_item_data['label'],
        "property_short_description": new_item_data['short_description'],
        "property_description": new_item_data['description'],
        "property_images": images_items,
        "property_id": new_item_data['pk'],
    }
    html_content = get_template('item/new_item_template.html').render(context)
    text_content = get_template('item/new_item_template.txt').render(context)
    newsletters_emails = [newsletter_email['email'] for newsletter_email in Newsletter.objects.filter(is_active=True).values('email')]
    msg = EmailMultiAlternatives(_('New property'), text_content, settings.EMAIL_HOST_USER, newsletters_emails[0:1], bcc=newsletters_emails[1:],)
    msg.attach_alternative(html_content, "text/html")
    msg.content_subtype = 'html'
    msg.mixed_subtype = 'related'
    for item_image in images_items:
        # Create an inline attachment
        image = MIMEImage(item_image.image.read())
        image.add_header('Content-ID', '<{}>'.format(item_image.image_filename))
        msg.attach(image)
    msg.send()