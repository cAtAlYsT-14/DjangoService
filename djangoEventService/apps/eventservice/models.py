from django.db import models
from django.utils.translation import ugettext_lazy as _
from .choices import EVENT_CHOICES

class AbstractAutoDate(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True,)
    modified = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        abstract = True

class Event(AbstractAutoDate):
    # event_id = models.IntegerField(
    #     _('Event Id'),
    #     blank=False, 
    #     null=False, 
    #     editable=False)
    event_type = models.SmallIntegerField(
        default=0, 
        choices=EVENT_CHOICES)
    triggered_browser = models.CharField(
        _('Browser'),
        max_length=50,
        blank=True)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ("-modified", "-created")
        get_latest_by = 'created'

    def __str__(self):
        return '%s - %s'% (str(self.id), EVENT_CHOICES[self.event_type][1])