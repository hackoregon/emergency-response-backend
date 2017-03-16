from django.test import TestCase
from data.models import Agency
from rest_framework.test import APIClient, RequestsClient

#Create your tests here.
class AgencyTestCase(TestCase):
    def test_agency_returns_attributes(self):
        agency = Agency.objects.get(agency_id=1)
        self.assertEqual(agency.agency_id, 1)
        self.assertEqual(agency.description, 'PORT OF PORTLAND')
        self.assertEqual(agency.statecode, '0291')

class IncidentInfoEndpointCase(TestCase):
    def test_200_response(self):
        client = APIClient()
        response = client.get('/incidents/info/?incident_id=1281359')
        assert response.status_code == 200
    def test_400_response(self):
        client = APIClient()
        response = client.get('/incidents/info/')
        assert response.status_code == 400
    def test_404_bad_incident_id_response(self):
        client = APIClient()
        response = client.get('/incidents/info/?incident_id=ab343')
        assert response.status_code == 404
    def test_404_not_found_incident_id_response(self):
        client = APIClient()
        response = client.get('/incidents/info/?incident_id=564343')
        assert response.status_code == 404
