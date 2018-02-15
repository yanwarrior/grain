from rest_framework import serializers

from companies.models import Company


class CompanyListGetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=250)


class CompanyListPostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
