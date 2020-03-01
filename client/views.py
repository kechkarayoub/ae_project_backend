# -*- coding: utf-8 -*-
from admin_data.models import AdminData
from backend.utils import get_list_social_links_images, send_email
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from settings_db.models import SettingsDb
from sociallink.views import get_list_social_links
import datetime
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
# #@csrf_exempt
def import_clients(request):
    """
    Import client list from excel file.
    """
    response = {}
    if request.method == 'POST':
        response.update({"success": True})
        if request.FILES.get("file"):
            file = request.FILES.get("file")
            response.update({"message": "Not yet done."})
        return JsonResponse(response, status=status.HTTP_200_OK)
    return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)


