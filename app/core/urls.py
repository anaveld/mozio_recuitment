from django.urls import include, path

from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', include('core.api.urls', namespace='api')),
]