from django.shortcuts import render
from django.db import connections
from django.db.utils import OperationalError
from django.db import models
from django.views.generic import TemplateView

#DRF Import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#local imports
from .models import Event
from .choices import EVENT_CHOICES, RESPONSE_TYPE

class DBHealth(APIView):
    '''
        API to check health of database. 
        Returns 'status' and 'connected' as true or false
    '''

    def get(self, request, *args, **kwargs):
        try:
            db_conn = connections['default']
            db_connection = db_conn.ensure_connection()
            connected = True
        except OperationalError:
            connected = False

        status_code = status.HTTP_200_OK if connected else status.HTTP_503_SERVICE_UNAVAILABLE
        resp_dict = {
            'status': 'DB is in Good Condition' if connected else 'Service Unavailable',
            'connected': connected
        }
        return Response(resp_dict, status=status_code)

class Events(APIView):
    '''
        Methods : GET and POST
        GET returns details of the events like total events, total unique events 
        and different browsers with their count
        POST put the data of Events in DB
    '''
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        resp_dict = {}

        try:
            event_objects = Event.objects.all()
            #Count of all event objects
            event_objects_count = event_objects.count()
            #Count of all unique event objects
            unique_events_count = event_objects.values("event_type").distinct().count()
            #Count of all different browsers with their count
            events_with_diffrent_browsers = event_objects.values("triggered_browser").\
                                                annotate(count=models.Count('pk')).\
                                                    order_by('triggered_browser')

            resp_dict.update({
                'count': event_objects_count,
                'unique_events': unique_events_count,
                'browsers': events_with_diffrent_browsers
            })
        except Exception as e:
            # Add logger here to log the error
            pass

        return Response(resp_dict, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        # Added try except to handle the string values for the event_type
        try:
            event_type = int(request.POST.get('event_type', 0)) or int(request.data.get('event_type', 0))
        except Exception as e:
            # Add logger to log the error
            event_type = 0
        browser_type = request.user_agent.browser.family
        msg = ''
        if(event_type in [1, 2, 3, 4]):
            if event_type in [2, 3]:
                Event.objects.create(
                    event_type = 2,
                    triggered_browser = browser_type,
                )
                Event.objects.create(
                    event_type = 3,
                    triggered_browser = browser_type,
                )
                # Add log here to log events for subscription
            else:
                Event.objects.create(
                    event_type = event_type,
                    triggered_browser = browser_type,
                )
                # Add log here to log other events

            msg = '%s' %(str(RESPONSE_TYPE.get(event_type)))
        else:
            return Response({
                'msg': 'Invalid Event. Bad Request!',
                'status_code': 400 
            }, status = status.HTTP_400_BAD_REQUEST)

        return Response({
            'msg': msg,
            'status_code': 200
        }, status = status.HTTP_200_OK)

class LandingPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingPageView, self).get_context_data(**kwargs)
        return context