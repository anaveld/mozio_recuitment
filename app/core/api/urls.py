from django.urls import include, path
from rest_framework import routers

from core.api import views

router = routers.DefaultRouter()
router.register(r'providers', views.ProviderViewSet, basename='providers')
router.register(r'service-areas', views.ServiceAreaViewSet, basename='service-areas')


app_name = 'api'


urlpatterns = [
    path('', include(router.urls)),
    path('search', views.search)
]
