import unittest
from django.test.client import Client
from booking.models import Event, Type
import datetime

class TypeTest(unittest.TestCase):
    def setUp(self):
        self.type = Type.objects.create(type='Live Performance')

    def testType(self):
        self.type_test = Type.objects.get(id = 1)
        self.failUnlessEqual(self.type_test.type, 'Live Performance')

class EventTest(unittest.TestCase):
    def setUp(self):
        self.date1=datetime.datetime(2009, 01, 01)
        self.event1 = Event.objects.create(title='test title', location='test venue', type_id=1,
            date=self.date1, street1='1234 test blvd.', street2='unit #test',
            city='testville', state='CO', zip='00000', price='$15', link='http://example.com',
            contact ='example@example.com', phone='000-000-0000', note='Test Note', public='1')

        self.date2=datetime.datetime(2020, 01, 01)
        self.event2 = Event.objects.create(title='test title', location='test venue', type_id=1,
            date=self.date2, street1='1234 test blvd.', street2='unit #test',
            city='testville', state='CO', zip='00000', price='$15', link='http://example.com',
            contact ='example@example.com', phone='000-000-0000', note='Test Note', public='1')

    def testPast(self):
        self.assertTrue(self.event1.past_event())
        self.assertFalse(self.event2.past_event())

    def testMap(self):
        self.assertEqual(self.event1.get_map(),
            'http://maps.google.com/maps?q=1234%20test%20blvd.%20unit%20#test%20testville%20CO%2000000')

    def testUpcomingView(self):
        self.client = Client()
        self.upcomming_response = self.client.get('/events/upcomming/')

        self.failUnlessEqual(self.upcomming_response.status_code, 200)
        self.failUnlessEqual(self.upcomming_response.context['events'][0].date, datetime.datetime(2020, 01, 01))

    def testPastView(self):
        self.client = Client()
        self.past_response = self.client.get('/events/past/')

        self.failUnlessEqual(self.past_response.status_code, 200)
        self.failUnlessEqual(self.past_response.context['events'][0].date, datetime.datetime(2009, 01, 01))
