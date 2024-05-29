from django.contrib.gis.geos import Point

from core.models import ServiceArea


def search_areas(x, y):
    point = Point(x, y)
    service_areas_queryset = ServiceArea.objects.filter(area__contains=point).order_by('-id')
    return service_areas_queryset
