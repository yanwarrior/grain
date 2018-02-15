from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from companies.models import Company
from companies.serializers import CompanyListGetSerializer, CompanyListPostSerializer


class CompanyListAPIView(APIView):

    def _get_queryset(self, *args, **kwargs):
        return Company.objects.all()

    def get(self, request, format=None):
        companies = self._get_queryset()
        serializer = CompanyListGetSerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanyListPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

