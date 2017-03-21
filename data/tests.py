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

class AgencyEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/agencies/')
        assert response.status_code == 200
    def test_list_description__icontains_query_works(self):
        response = self.client.get('/agencies/?description__icontains=portland')
        assert response.status_code == 200
    def test_retrieve_200_response(self):
        response = self.client.get('/agencies/1/')
        assert response.status_code == 200

class AlarmLevelsEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/alarmlevels/')
        assert response.status_code == 200
    def test_retrieve_200_response(self):
        response = self.client.get('/alarmlevels/1/')
        assert response.status_code == 200

class FireBlocksEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/fireblocks/')
        assert response.status_code == 200
    def test_retrieve_200_response(self):
        response = self.client.get('/fireblocks/471/')
        assert response.status_code == 200
    def geofilter_query_200_response(self):
        response = self.client.get('/fireblock/?lat=45.520697&lon=-122.677345')
        assert response.status_code == 200
class IncidentInfoEndpointCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_200_response(self):
        response = self.client.get('/incidents/info/?incident_id=1281359')
        assert response.status_code == 200
    def test_400_response(self):
        response = self.client.get('/incidents/info/')
        assert response.status_code == 400
    def test_404_bad_incident_id_response(self):
        response = self.client.get('/incidents/info/?incident_id=ab343')
        assert response.status_code == 404
    def test_404_not_found_incident_id_response(self):
        response = self.client.get('/incidents/info/?incident_id=564343')
        assert response.status_code == 404

class FMAListEndpointCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_200_response(self):
        response = self.client.get('/fmas/')
        assert response.status_code == 200
