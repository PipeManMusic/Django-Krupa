from danielworth.booking.models import Event
from django.shortcuts import render_to_response
import datetime

def upcomming_events(requiest):
    upcomming_events = Event.upcomming_objects.all()
    template = 'upcomming_events.html'
    return render_to_response(template, {'events' : upcomming_events})

def past_events(request):
    past_events = Event.past_objects.all()
    template = 'past_events.html'
    return render_to_response(template, {'events' : past_events})
