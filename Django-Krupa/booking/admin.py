from danielworth.booking.models import *
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('title', 'date', 'location', 'city', 'state')

admin.site.register(Event, EventAdmin)
