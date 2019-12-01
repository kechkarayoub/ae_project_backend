# -*- coding: utf-8 -*-
from .models import Funding
from .serializers import FundingSerializer
from admin_data.models import AdminData
from backend.utils import send_email, get_list_social_links_images
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from email.mime.image import MIMEImage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from settings_db.models import SettingsDb
from sociallink.views import get_list_social_links


@api_view(['GET'])
def funding_list(request):
    """
    List funding.
    """
    funding = Funding.objects.filter().order_by('-createdAt')
    serializer = FundingSerializer(funding, context={'request': request}, many=True)
    return Response({
        'data': serializer.data
    })


@api_view(['POST'])
def send_funding_email(request):
    """
    Send mail.
    """
    data = request.data
    funding = Funding.objects.get(id=data.get("funding_id"))
    subject = _("Client funding email")
    context = {
        "email": funding.user_email,
        "environment": settings.ENVIRONMENT,
        "first_name": funding.first_name,
        "last_name": funding.last_name,
        "logo_url": settings.BACKEND_URL_ROOT + static("contact/images/logo.jpg"),
        "site_name": SettingsDb.get_site_name(),
        "site_url_root": settings.SITE_URL_ROOT,
        "show_unsubscribe_url": False,
        "social_links": get_list_social_links(),
        "social_links_images": get_list_social_links_images()
    }
    try:
        html_admin_content = get_template('funding/funding_admin_template.html').render(context)
        text_admin_content = get_template('funding/funding_admin_template.txt').render(context)
        send_email(subject, text_admin_content, funding.user_email, AdminData.get_admin_email(), html_admin_content)
        html_bank_content = get_template('funding/funding_bank_template.html').render(context)
        text_bank_content = get_template('funding/funding_bank_template.txt').render(context)
        send_email(subject, text_bank_content, funding.user_email, funding.bank.email, html_bank_content)
        return Response({
            'success': True
        })
    except:
        return Response({
            'success': False,
            'message': _("An error has occurred. Check your connection.")
        })
