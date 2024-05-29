from django.core.exceptions import BadRequest
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.api.serializers import ProviderSerializer, SearchDataSerializer, ServiceAreaSerializer
from core.models import Provider, ServiceArea
from core.search import search_areas


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


@api_view()
def search(request):
    serializer = SearchDataSerializer(data={
        'x': request.GET.get('x'),
        'y': request.GET.get('y'),
    })
    if not serializer.is_valid():
        raise BadRequest('You need to provide X and Y coordinates.')
    data = serializer.data
    search_results_queryset = search_areas(data['x'], data['y'])
    serialized_results = ServiceAreaSerializer(search_results_queryset, many=True)
    return Response(serialized_results.data)
