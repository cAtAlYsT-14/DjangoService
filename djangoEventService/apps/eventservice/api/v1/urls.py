from django.urls import re_path, include
from .views import DBHealth

app_name = "event_service_apis"

urlpatterns = [
    # re_path(r'^health/$', DBHealth.as_view(), name='db_health')
]