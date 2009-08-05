from django.db import models
from django.contrib.localflavor.us.models import *

class Group(models.Model):
    name = models.CharField('Name', max_length=50)
    startdate = models.DateField('Started')
    enddate = models.DateField('Ended', blank=True)
    history = models.TextField('History', blank=True)
    link = models.URLField('Link', blank=True)

    def __unicode__(self):
       return  self.name

class License(models.Model):
    type = models.CharField('License Type', max_length=100)
    link = models.URLField('Link', blank=True)

    def __unicode__(self):
        return self.type

class PRO(models.Model):
    name = models.CharField('Name', max_length=50)
    street1 = models.CharField('Street Address', max_length=50)
    street2 = models.CharField('Street Address 2', max_length=50, blank=True)
    city = models.CharField('City', max_length=50)
    state = USStateField('State')
    zip = models.PositiveIntegerField('Zip Code')
    link = models.URLField('Link', blank=True)
    contact = models.EmailField('Contact E-mail', blank=True)
    phone = PhoneNumberField('Contact Number', blank=True)

    def __unicode__(self):
        return '%s, %s' %(self.name, self.city)

class Publisher(models.Model):
    name = models.CharField('Name', max_length=50)
    street1 = models.CharField('Street Address', max_length=50)
    street2 = models.CharField('Street Address 2', max_length=50, blank=True)
    city = models.CharField('City', max_length=50)
    state = USStateField('State')
    zip = models.PositiveIntegerField('Zip Code')
    link = models.URLField('Link', blank=True)
    contact = models.EmailField('Contact E-mail', blank=True)
    phone = PhoneNumberField('Contact Number', blank=True)
    pro = models.ForeignKey(PRO, null=True)

    def __unicode__(self):
        return self.name
    
class Artist(models.Model):
    firstname = models.CharField('Artist First Name', max_length=50)
    lastname = models.CharField('Artist Last Name', max_length=50)
    performance = models.ManyToManyField('Performance', through='ArtistPerformance')
    pro = models.ForeignKey(PRO, blank=True, null=True)
    birthday = models.DateField('Birthday', blank=True, null=True)
    birthcity = models.CharField('City of Birth', max_length=50, blank=True)
    birthstate= USStateField('State of Birth', blank=True) 
    groups = models.ManyToManyField('Group', through='GroupMembership', blank=True,  null=True)

    def __unicode__(self):
        return '%s, %s' %(self.lastname, self.firstname)

class GroupMembership(models.Model):
    artist = models.ForeignKey(Artist)
    group = models.ForeignKey(Group)
    startdate = models.DateField('Joined')
    enddate = models.DateField('Left', blank=True, null=True)

    def __unicode(self):
        return '%s - %s' %(self.artist, self.group)

class Song(models.Model):
    title = models.CharField('Title', max_length=50)
    writer = models.ManyToManyField(Artist)
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    copyrightdate = models.DateField('Copyrighted')
    copyrightnum = models.PositiveIntegerField('Copyright Number', blank=True)
    license = models.ForeignKey(License)

    def __unicode__(self):
        return self.title

class Studio(models.Model):
    name = models.CharField('Name', max_length=50)
    street1 = models.CharField('Street Address', max_length=50)
    street2 = models.CharField('Street Address 2', max_length=50, blank=True)
    city = models.CharField('City', max_length=50)
    state = USStateField('State')
    zip = models.PositiveIntegerField('Zip Code')
    link = models.URLField('Link', blank=True)
    contact = models.EmailField('Contact E-mail', blank=True)
    phone = PhoneNumberField('Contact Number', blank=True)

    def __unicode__(self):
        return self.name

class Performance(models.Model):
    group = models.ForeignKey(Group, blank=True, null=True)
    song = models.ForeignKey(Song)
    datestart = models.DateField('Start Date')
    datestop = models.DateField('End Date', blank=True, null=True)
    studio = models.ForeignKey(Studio, blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.song

class Label(models.Model):
    name = models.CharField('Name', max_length=50)
    street1 = models.CharField('Street Address', max_length=50)
    street2 = models.CharField('Street Address 2', max_length=50, blank=True)
    city = models.CharField('City', max_length=50)
    state = USStateField('State')
    zip = models.PositiveIntegerField('Zip Code')
    link = models.URLField('Link', blank=True)
    contact = models.EmailField('Contact E-mail', blank=True)
    phone = PhoneNumberField('Contact Number', blank=True)

    def __unicode__(self):
        return self.name

class Role(models.Model):
    name = models.CharField('Role', max_length=50)

    def __unicode__(self):
        return self.name

class ArtistPerformance(models.Model):
    artist = models.ForeignKey(Artist)
    performance = models.ForeignKey(Performance)
    role = models.ManyToManyField(Role)

    def __unicode__(self):
        return '%s' % self.artist

class Distributor(models.Model):
    name = models.CharField('Name', max_length=50)
    street1 = models.CharField('Street Address', max_length=50)
    street2 = models.CharField('Street Address 2', max_length=50, blank=True)
    city = models.CharField('City', max_length=50)
    state = USStateField('State')
    zip = models.PositiveIntegerField('Zip Code')
    link = models.URLField('Link', blank=True)
    contact = models.EmailField('Contact E-mail', blank=True)
    phone = PhoneNumberField('Contact Number', blank=True)

    def __unicode__(self):
        return self.name
  
class Album(models.Model):
    title = models.CharField('Title', max_length=50)
    tracks = models.ManyToManyField(Performance)
    label = models.ManyToManyField(Label, blank=True, null=True)
    catnum = models.CharField('Catalog Number', max_length=50, blank=True)
    upc = models.PositiveIntegerField('UPC Code', blank=True)
    distributor = models.ForeignKey(Distributor, blank=True, null=True)
    compilation = models.BooleanField('Compilation')

    def __unicode__(self):
       return self.title
