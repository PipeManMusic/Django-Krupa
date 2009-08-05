from django.db import models
from django.contrib.localflavor.us.models import *
import datetime

class Event(models.Model):
    """
    Event provides for tracking different types of events.
    """

    title = models.CharField('Title of Event', max_length=50)
    type = models.ForeignKey(Type)
    location = models.CharField('Location of Event', max_length=50)
    date = models.DateTimeField('Event Date')
    street1 = models.CharField('Street Address', max_length=50, blank=True)
    street2 = models.CharField('Street Address 2', max_length=50, blank=True)
    city = models.CharField('City', max_length=50, blank=True)
    state = USStateField('State', blank=True)
    zip = models.PositiveIntegerField('Zip Code', blank=True)
    price = models.CharField('Ticket Price(s)', max_length=25, blank=True)
    link = models.URLField('Link', blank=True)
    contact = models.EmailField('Contact E-mail', blank=True)
    phone = PhoneNumberField('Contact Phone Number', blank=True)
    note = models.TextField('Notes', blank=True)
    created = models.DateTimeField('Creation Date', auto_now_add=True)
    edited = models.DateTimeField('Last Edited', auto_now=True)
    public = models.BooleanField('Public')

    class Meta:
        ordering = ['date', 'title']

    def __unicode__(self):
        return self.title

    def past_event(self):
        """
        Returns true if the performance.date is before todays date.
        """

        return self.date <= datetime.datetime.today()

    def get_map(self):
        """
        Returns a google map url for the Performance
        """

        self.address1 = self.street1.split(' ')
        self.address2 = self.street2.split(' ')
        self.url = 'http://maps.google.com/maps?q='

        for word in self.address1:
            self.url = self.url + word + '%20'

        for word in self.address2:
            self.url = self.url + word + '%20'

        self.url = self.url + self.city + '%20' + self.state + '%20' + '%s' % self.zip
        return self.url

    def get_date(self):
        return self.date
    def upcomming_events(self):
        return self.
class Type(models.Model):
    """
    Type provides a catagory for different types of events
    """

    type = models.CharField('Type of Event', max_length=50)

    def __unicode__(self):
        return self.type
