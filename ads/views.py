from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdSerializer
from .models import Ad


class AdListView(APIView):
    serializer_class = AdSerializer

    def get(self, request):
        querset = Ad.objects.filter(is_public=True)
        serializer = AdSerializer(instance=querset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
