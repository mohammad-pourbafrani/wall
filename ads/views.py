from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdSerializer
from .models import Ad
from .pagination import StandardResultPagInation


class AdListView(APIView , StandardResultPagInation):
    serializer_class = AdSerializer

    def get(self, request):
        queryset = Ad.objects.filter(is_public=True)
        result = self.paginate_queryset(queryset , request)
        serializer = AdSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)
