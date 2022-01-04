from django.urls import re_path, include
from .views import DBHealth, Events, LandingPageView

app_name = "event_service"

urlpatterns = [
    re_path(r'^$', LandingPageView.as_view(), name='landing_page'),
    re_path(r'^health/$', DBHealth.as_view(), name='db_health'),
    re_path(r'^events/$', Events.as_view(), name='events')
]