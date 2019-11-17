# -*- coding: utf-8 -*-
from .models import Funding
from .serializers import FundingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


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

