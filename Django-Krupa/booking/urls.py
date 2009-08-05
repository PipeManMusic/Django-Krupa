from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from danielworth.booking.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^calendar/', direct_to_template, {'template' : 'base.html'}, name='calendar',),
    url(r'^upcomming/', upcomming_events, name='upcomming'),    
    url(r'^past/', past_events, name='past')    
)
