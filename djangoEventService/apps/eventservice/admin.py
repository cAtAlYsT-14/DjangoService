from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_type', 'triggered_browser')
    search_fields = ('event_type',)

admin.site.register(Event, EventAdmin)
