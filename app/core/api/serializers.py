from django.db.models import fields
from rest_framework import serializers
from core.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'email', 'language', 'currency')


class ServiceAreaSerializer(serializers.ModelSerializer):
    provider = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all())

    class Meta:
        model = ServiceArea
        fields = ('provider', 'name', 'price', 'area')


class SearchDataSerializer(serializers.Serializer):
    x = serializers.FloatField()
    y = serializers.FloatField()

    class Meta:
        fields = ('x', 'y')
