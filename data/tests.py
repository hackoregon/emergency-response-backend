from django.test import TestCase
from data.models import Agency

# Create your tests here.
class AgencyTestCase(TestCase):
    def test_agency_returns_attributes(self):
        agency = Agency.objects.get(agency_id=1)
        self.assertEqual(agency.agency_id, 1)
        self.assertEqual(agency.description, 'PORT OF PORTLAND')
        self.assertEqual(agency.statecode, '0291')
